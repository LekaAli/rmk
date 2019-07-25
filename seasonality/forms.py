from django import forms
from .import models

class SeasonalityForm(forms.ModelForm):
    class Meta:
        model = models.ProductSeasonality
        fields = '__all__'
