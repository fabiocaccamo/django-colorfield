# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.template.loader import render_to_string


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

    def render(self, name, value, attrs=None, renderer=None):
        return render_to_string(self.template_name, { 'widget': self })
