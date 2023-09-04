import os
import shutil

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.files import File
from django.forms import fields_for_model
from django.test import TestCase

from colorfield.fields import ColorField
from tests.models import (
    COLOR_PALETTE,
    Color,
    ColorChoices,
    ColorFieldRGBFormat,
    ColorImageField,
    ColorImageFieldAndDefault,
    ColorImageFieldAndFormat,
    ColorInvalidImageField,
    ColorNoImageField,
    ColorNull,
    ColorSamples,
)


class ColorFieldTestCase(TestCase):
    def setUp(self):
        self.delete_media()

    def tearDown(self):
        self.delete_media()

    @classmethod
    def delete_media(cls):
        path = settings.MEDIA_ROOT
        if os.path.exists(path):
            shutil.rmtree(path)

    @classmethod
    def get_images_input_dir(cls):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    @classmethod
    def save_image_to_field_from_path(cls, field, path, save=True):
        path = os.path.join(cls.get_images_input_dir(), path)
        with open(path, "rb") as image:
            name = os.path.basename(path)
            field.save(name, content=File(image), save=save)

    def test_model_formfield_doesnt_raise(self):
        """
        Adding a ColorField to a model should not fail in 2.2LTS.
        """
        try:
            fields_for_model(Color())
        except AttributeError:
            self.fail("Raised Attribute Error")

    def test_model_formfield_with_samples_and_choices_fails(self):
        """
        Checks that supplying a ColorField with both samples
        and choices options fails (mutually exclusive).
        """
        with self.assertRaises(ImproperlyConfigured):
            ColorField(choices=COLOR_PALETTE, samples=COLOR_PALETTE)

    def test_clean_field_choices(self):
        """
        Checks that supplying a ColorField with the samples kwarg works,
        and that it accepts valid values outside the predefined choices.
        """
        # 1. Test with predefined choice
        obj = ColorChoices()
        obj.color = ColorChoices.COLOR_CHOICES[0][0]
        try:
            obj.full_clean()
        except ValidationError as e:
            self.fail(
                "Failed to assign predefined palette choice "
                f"to ColorField model instance. Message: {e}"
            )

        # 2. Test with value outside of the choices
        other_value = "#35B6A3"
        obj.color = other_value
        with self.assertRaises(ValidationError):
            obj.full_clean()

    def test_clean_field_samples(self):
        """
        Checks that supplying a ColorField with the samples kwarg works,
        and that it accepts valid values outside the predefined choices.
        """
        # 1. Test with predefined choice
        obj = ColorSamples()
        obj.color = ColorSamples.COLOR_SAMPLES[0][0]
        try:
            obj.full_clean()
        except ValidationError as e:
            self.fail(
                "Failed to assign predefined palette choice "
                f"to ColorField model instance. Message: {e}"
            )

        # 2. Test with value outside of the choices
        other_value = "#35B6A3"
        obj.color = other_value
        try:
            obj.full_clean()
        except ValidationError as e:
            self.fail(
                "Failed to assign value outside palette choices "
                f"to ColorField model instance. Message: {e}"
            )

    def test_model_with_null(self):
        obj = ColorNull()
        obj.save()
        self.assertEqual(obj.color, None)

    def test_model_with_invalid_image_field_type(self):
        obj = ColorInvalidImageField()
        with self.assertRaises(ImproperlyConfigured):
            obj.save()

    def test_model_with_not_existing_image_field(self):
        obj = ColorNoImageField()
        with self.assertRaises(ImproperlyConfigured):
            obj.save()

    def test_model_with_image_field_empty(self):
        obj = ColorImageField()
        obj.save()
        self.assertEqual(obj.color, "")

    def test_model_with_image_field_empty_and_default(self):
        obj = ColorImageFieldAndDefault()
        obj.save()
        self.assertEqual(obj.color, "#FF0000")

    def test_model_with_image(self):
        model_class = ColorImageField
        obj = model_class()
        filename = "django.png"
        self.save_image_to_field_from_path(obj.image, filename)
        obj.save()
        # ensure the image has been saved correctly
        self.assertTrue(obj.image.path.endswith(filename))
        expected_color = "#082D20"
        # check in-memory value
        self.assertEqual(obj.color, expected_color)
        # check stored value
        obj_saved = model_class.objects.get(pk=obj.pk)
        self.assertEqual(obj_saved.color, expected_color)

    def test_model_with_image_and_format(self):
        model_class = ColorImageFieldAndFormat
        obj = model_class()
        filename = "django.png"
        self.save_image_to_field_from_path(obj.image, filename)
        obj.save()
        # ensure the image has been saved correctly
        self.assertTrue(obj.image.path.endswith(filename))
        expected_color = "#082D20FF"
        # check in-memory value
        self.assertEqual(obj.color, expected_color)
        # check stored value
        obj_saved = model_class.objects.get(pk=obj.pk)
        self.assertEqual(obj_saved.color, expected_color)

    def test_model_rgb_formats(self):
        obj = ColorFieldRGBFormat(
            color_rgb="rgb(123, 123, 123)",
            color_rgba="rgba(5, 10, 128, 0.5)",
        )
        obj.save()
        # check in-memory values
        self.assertEqual(obj.color_rgb, "rgb(123, 123, 123)")
        self.assertEqual(obj.color_rgba, "rgba(5, 10, 128, 0.5)")
        # check stored value
        obj_saved = ColorFieldRGBFormat.objects.get(pk=obj.pk)
        self.assertEqual(obj_saved.color_rgb, "rgb(123, 123, 123)")
        self.assertEqual(obj_saved.color_rgba, "rgba(5, 10, 128, 0.5)")
