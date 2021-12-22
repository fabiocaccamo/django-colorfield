# -*- coding: utf-8 -*-

from colorfield.fields import ColorField

from django.db import models


COLOR_PALETTE = [
    ('#FFFFFF', 'white'),
    ('#000000', 'black'),
]


class Color(models.Model):

    color = ColorField(blank=True)

    class Meta:
        app_label = 'tests'


class ColorNull(models.Model):

    color = ColorField(null=True)

    class Meta:
        app_label = 'tests'


class ColorChoices(models.Model):

    COLOR_CHOICES = COLOR_PALETTE

    color = ColorField(blank=True, choices=COLOR_CHOICES)

    class Meta:
        app_label = 'tests'


class ColorSamples(models.Model):

    COLOR_SAMPLES = COLOR_PALETTE

    color = ColorField(blank=True, samples=COLOR_SAMPLES)

    class Meta:
        app_label = 'tests'


class ColorNoImageField(models.Model):

    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorInvalidImageField(models.Model):

    image = models.CharField(blank=True, max_length=10)
    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorImageField(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image')

    class Meta:
        app_label = 'tests'


class ColorImageFieldAndDefault(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image', default='#FF0000')

    class Meta:
        app_label = 'tests'


class ColorImageFieldAndFormat(models.Model):

    image = models.ImageField(blank=True, upload_to='temp')
    color = ColorField(image_field='image', format='hexa')

    class Meta:
        app_label = 'tests'
