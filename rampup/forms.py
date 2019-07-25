from django import forms
from .import models

class CapacityRampUpForm(forms.ModelForm):
    class Meta:
        model = models.CapacityRampUp
        fields = '__all__'
    

