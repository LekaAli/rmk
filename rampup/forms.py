from django import forms
from rampup.models import ProductRampUp


class CapacityRampUpForm(forms.ModelForm):
    class Meta:
        model = ProductRampUp
        fields = '__all__'
    

