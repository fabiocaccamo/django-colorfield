from django import forms

from colorfield.forms import ColorField

from .models import Color


class ColorForm(forms.ModelForm):
    color_ro = ColorField(label="Color disabled", disabled=True, required=False)

    class Meta:
        model = Color
        fields = forms.ALL_FIELDS
