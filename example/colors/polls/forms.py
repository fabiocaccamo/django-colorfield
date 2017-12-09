from django.forms import ModelForm
from .models import Poll, Choice

class ChoiceForm(ModelForm):
     class Meta:
         model = Choice
         fields = ['color']
