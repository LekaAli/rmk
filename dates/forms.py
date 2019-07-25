
from django import forms
from .import models


class DatesForm(forms.ModelForm):
    class Meta:
        model = models.Dates
        fields = '__all__'