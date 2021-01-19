# -*- coding: utf-8 -*-

from django import forms
from django.forms import fields_for_model
from django.db import models
from django.test import TestCase

from colorfield.fields import ColorField


class ColoredModel(models.Model):
    colors = ColorField(blank=True)

    class Meta:
        app_label = 'colorfield'


class ColorFieldTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_model_formfield_doesnt_raise(self):
        """Adding a ColoredField to a model should not fail in 2.2LTS
        """
        try:
            fields_for_model(ColoredModel())
        except AttributeError:
            self.fail('Raised Attribute Error')
