# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.db import models
from django.forms import fields_for_model
from django.test import TestCase

from colorfield.fields import ColorField

class ColoredModel(models.Model):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black")
    ]

    colors = ColorField(blank=True, samples=COLOR_CHOICES)

    class Meta:
        app_label = 'colorfield'


class ColorFieldTestCase(TestCase):

    def setUp(self):
        self.instance = ColoredModel()

    def tearDown(self):
        pass

    def test_model_formfield_doesnt_raise(self):
        """Adding a ColoredField to a model should not fail in 2.2LTS
        """
        try:
            fields_for_model(ColoredModel())
        except AttributeError:
            self.fail('Raised Attribute Error')
    
    def test_model_formfield_with_samples_and_choices_fails(self):
        """
        Checks that supplying a ColorField with both samples and choices options fails (mutually exclusive)
        """
        with self.assertRaises(ImproperlyConfigured):
            ColorField(choices=ColoredModel.COLOR_CHOICES, samples=ColoredModel.COLOR_CHOICES)

    def test_clean_field_samples(self):
        """
        Checks that supplying a ColorField with the samples kwarg works, and that it accepts valid values outside the predefined choices
        """
        # 1. Test with predefined choice
        self.instance.colors = self.instance.COLOR_CHOICES[0][0]
        try:
            self.instance.full_clean()
        except ValidationError as e:
            self.fail('Failed to assign predefined palette choice to ColorField model instance. Message: {}'.format(e))
        
        # 2. Test with value outside of the choices
        other_value = '#35B6A3'
        self.instance.colors = other_value
        try:
            self.instance.full_clean()
        except ValidationError as e:
            self.fail('Failed to assign value outside palette choices to ColorField model instance. Message: {}'.format(e))
