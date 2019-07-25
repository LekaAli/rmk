from django import forms
from .import models


class InflationForm(forms.ModelForm):
    class Meta:
        model = models.Inflation
        fields = '__all__'    
