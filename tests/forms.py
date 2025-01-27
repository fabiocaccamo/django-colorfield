from django import forms
from colorfield.forms import ColorField


class BasicForm(forms.Form):
    color = ColorField(initial="#FF0000")
