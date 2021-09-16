# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings


class ColorWidget(forms.TextInput):

    template_name = 'colorfield/color.html'

    class Media:
        if settings.DEBUG:
            js = [
                'colorfield/jscolor/jscolor.js',
                'colorfield/colorfield.js',
            ]
        else:
            js = [
                'colorfield/jscolor/jscolor.min.js',
                'colorfield/colorfield.js',
            ]
