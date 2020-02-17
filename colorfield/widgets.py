# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.template.loader import render_to_string


class ColorWidget(forms.Widget):

    class Media:
        if settings.DEBUG:
            js = ['colorfield/jscolor/jscolor.js']
        else:
            js = ['colorfield/jscolor/jscolor.min.js']

    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        is_required = self.is_required
        return render_to_string('colorfield/color.html', locals())

    def value_from_datadict(self, data, files, name):
        value = super(ColorWidget, self).value_from_datadict(data, files, name)
        return '#{}'.format(value) if value else value
