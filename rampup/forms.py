from django import forms
from rampup.models import RampUp


class CapacityRampUpForm(forms.ModelForm):
    class Meta:
        model = RampUp
        fields = '__all__'
    

