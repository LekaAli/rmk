from django import forms
from .import models

class RevenueForm(forms.ModelForm):
    class Meta:
        model = models.Revenue
        fields = '__all__'
