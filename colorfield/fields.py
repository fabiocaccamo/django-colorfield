# -*- coding: utf-8 -*-

from colorfield.widgets import ColorWidget

import django
from django.core.validators import RegexValidator
from django.db import models
if django.VERSION >= (2, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

import re

COLOR_RE = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
color_validator = RegexValidator(COLOR_RE, _('Enter a valid color.'), 'invalid')


class ColorField(models.CharField):
    default_validators = [color_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^colorfield\\.fields\\.ColorField"])
except ImportError:
    pass
