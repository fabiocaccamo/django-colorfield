# -*- coding: utf-8 -*-

from django import VERSION as DJANGO_VERSION

from colorfield.utils import get_image_file_background_color
from colorfield.validators import color_hex_validator, color_hexa_validator
from colorfield.widgets import ColorWidget

if DJANGO_VERSION >= (1, 8):
    from django.core.exceptions import FieldDoesNotExist
else:
    FieldDoesNotExist = Exception
from django.core.exceptions import ImproperlyConfigured

from django.db.models import CharField, signals
from django.db.models.fields.files import ImageField


VALIDATORS_PER_FORMAT = {"hex": color_hex_validator, "hexa": color_hexa_validator}

DEFAULT_PER_FORMAT = {"hex": "#FFFFFF", "hexa": "#FFFFFFFF"}


class ColorField(CharField):

    default_validators = []

    def __init__(self, *args, **kwargs):
        # works like Django choices, but does not restrict input to the given choices
        self.samples = kwargs.pop("samples", None)
        self.format = kwargs.pop("format", "hex").lower()
        if self.format not in ["hex", "hexa"]:
            raise ValueError("Unsupported color format: {}".format(self.format))
        self.default_validators = [VALIDATORS_PER_FORMAT[self.format]]

        self.image_field = kwargs.pop("image_field", None)
        if self.image_field:
            kwargs.setdefault("blank", True)

        kwargs.setdefault("max_length", 18)
        if kwargs.get("null"):
            kwargs.setdefault("blank", True)
            kwargs.setdefault("default", None)
        elif kwargs.get("blank"):
            kwargs.setdefault("default", "")
        else:
            kwargs.setdefault("default", DEFAULT_PER_FORMAT[self.format])
        super(ColorField, self).__init__(*args, **kwargs)

        if self.choices and self.samples:
            raise ImproperlyConfigured(
                "Invalid options: 'choices' and 'samples' are mutually exclusive, "
                "you can set only one of the two for a ColorField instance."
            )

    def formfield(self, **kwargs):
        palette = []
        if self.choices:
            choices = self.get_choices(include_blank=False)
            palette = [choice[0] for choice in choices]
        elif self.samples:
            palette = [choice[0] for choice in self.samples]
        kwargs["widget"] = ColorWidget(
            attrs={
                "default": self.get_default(),
                "format": self.format,
                "palette": palette,
                # # this will be used to hide the widget color spectrum if choices is defined:
                # 'palette_choices_only': bool(self.choices),
            }
        )
        return super(ColorField, self).formfield(**kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(ColorField, self).contribute_to_class(cls, name, **kwargs)
        if cls._meta.abstract:
            return
        if self.image_field:
            signals.post_save.connect(self._update_from_image_field, sender=cls)

    def deconstruct(self):
        name, path, args, kwargs = super(ColorField, self).deconstruct()
        kwargs["samples"] = self.samples
        kwargs["image_field"] = self.image_field
        return name, path, args, kwargs

    def _get_image_field_color(self, instance):
        color = ""
        image_file = getattr(instance, self.image_field)
        if image_file:
            alpha = self.format == "hexa"
            if DJANGO_VERSION >= (2, 0):
                # https://stackoverflow.com/a/3033986/2096218
                with image_file.open() as _:
                    color = get_image_file_background_color(image_file, alpha)
            else:
                # https://stackoverflow.com/a/3033986/2096218
                image_file.open()
                color = get_image_file_background_color(image_file, alpha)
                image_file.close()
        return color

    def _update_from_image_field(self, instance, created, *args, **kwargs):
        if not instance or not instance.pk or not self.image_field:
            return
        # check if the field is a valid ImageField
        try:
            field_cls = instance._meta.get_field(self.image_field)
            if not isinstance(field_cls, ImageField):
                raise ImproperlyConfigured(
                    'Invalid "image_field" field type, '
                    'expected an instance of "models.ImageField".'
                )
        except FieldDoesNotExist as _:
            raise ImproperlyConfigured(
                'Invalid "image_field" field name, '
                '"{}" field not found.'.format(self.image_field)
            )
        # update value from picking color from image field
        color = self._get_image_field_color(instance)
        color_field_name = self.attname
        color_field_value = getattr(instance, color_field_name, None)
        if color_field_value != color:
            color_field_value = color or self.default
            # update in-memory value
            setattr(instance, color_field_name, color_field_value)
            # update stored value
            manager = instance.__class__.objects
            manager.filter(pk=instance.pk).update(
                **{color_field_name: color_field_value}
            )
