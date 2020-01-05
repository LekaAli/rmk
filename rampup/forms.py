from django import forms
from rmkplatform.constants import MONTHS, TYPE


class CapacityRampUpForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    rampup_type = forms.ChoiceField(widget=forms.Select(), choices=TYPE, initial='Select Type')
    rampup_values = forms.CharField(widget=forms.SelectMultiple)
    year = forms.CharField()
    will_roll_over = forms.BooleanField()
    
    name.widget.attrs['placeholder'] = 'Ramp Up Description'


class CapacityRampUpValuesForm(forms.Form):
    month = forms.ChoiceField(widget=forms.Select(), choices=MONTHS)
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'
