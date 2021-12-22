# -*- coding: utf-8 -*-

from colorfield.fields import ColorField

from django.db import models


COLOR_PALETTE = [
    ('#FFFFFF', 'white'),
    ('#000000', 'black'),
]


class ColorModel(models.Model):

    color = ColorField(blank=True)

    class Meta:
        app_label = 'tests'


class ColorModelWithNull(models.Model):

    color = ColorField(null=True)

    class Meta:
        app_label = 'tests'


class ColorModelWithChoices(models.Model):

    COLOR_CHOICES = COLOR_PALETTE

    color = ColorField(blank=True, choices=COLOR_CHOICES)

    class Meta:
        app_label = 'tests'


class ColorModelWithSamples(models.Model):

    COLOR_SAMPLES = COLOR_PALETTE

    color = ColorField(blank=True, samples=COLOR_SAMPLES)

    class Meta:
        app_label = 'tests'


class ColorModelWithNotExistingImageField(models.Model):

    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorModelWithInvalidImageFieldType(models.Model):

    image = models.CharField(blank=True, max_length=10)
    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorModelWithImageField(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorModelWithImageFieldAndDefault(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image', default='#FF0000')

    class Meta:
        app_label = 'tests'


class ColorModelWithImageFieldAndFormat(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image', format='hexa')

    class Meta:
        app_label = 'tests'
