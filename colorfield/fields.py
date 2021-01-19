# -*- coding: utf-8 -*-

import re
from colorfield.widgets import ColorWidget

import django
from django.core.validators import RegexValidator
from django.db import models
if django.VERSION >= (2, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _


COLOR_HEX_RE = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
color_hex_validator = RegexValidator(
    COLOR_HEX_RE, _('Enter a valid hex color, eg. #000000'), 'invalid')

COLOR_HEXA_RE = re.compile('#([A-Fa-f0-9]{8}|[A-Fa-f0-9]{4})$')
color_hexa_validator = RegexValidator(
    COLOR_HEXA_RE, _('Enter a valid hexa color, eg. #00000000'), 'invalid')

VALIDATORS_PER_FORMAT = {
    'hex': color_hex_validator,
    'hexa': color_hexa_validator
}

DEFAULT_PER_FORMAT = {
    'hex': '#FFFFFF',
    'hexa': '#FFFFFFFF'
}


class ColorField(models.CharField):

    default_validators = []

    def __init__(self, *args, **kwargs):
        self.format = kwargs.pop('format', 'hex').lower()
        if self.format not in ['hex', 'hexa']:
            raise ValueError('Unsupported color format: {}'.format(self.format))
        self.default_validators = [VALIDATORS_PER_FORMAT[self.format]]

        kwargs.setdefault('max_length', 18)
        if kwargs.get('null'):
            kwargs.setdefault('blank', True)
            kwargs.setdefault('default', None)
        elif kwargs.get('blank'):
            kwargs.setdefault('default', '')
        else:
            kwargs.setdefault('default', DEFAULT_PER_FORMAT[self.format])
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        palette = []
        if self.choices:
            choices = self.get_choices(include_blank=False)
            palette = [choice[0] for choice in choices]
        kwargs['widget'] = ColorWidget(attrs={
            'default': self.get_default(),
            'format': self.format,
            'palette': palette,
        })
        return super(ColorField, self).formfield(**kwargs)
