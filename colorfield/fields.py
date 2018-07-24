#!/usr/bin/env python

import re

from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


class ColorWidget(forms.Widget):
    class Media:
        if settings.DEBUG:
            js = ['colorfield/jscolor/jscolor.js']
        else:
            js = ['colorfield/jscolor/jscolor.min.js']

    def render(self, name, value, attrs=None, renderer=None, **_kwargs):
        is_required = self.is_required
        return render_to_string('colorfield/color.html', locals())

    def value_from_datadict(self, data, files, name):
        ret = super(ColorWidget, self).value_from_datadict(data, files, name)
        ret = '#%s' % ret if ret else ret
        return ret


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorfield\.fields\.ColorField"])
except ImportError:
    pass

# vim: et sw=4 sts=4
