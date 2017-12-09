from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='addclass')
def addclass(field, cls):
   return field.as_widget(attrs={"class": cls})
