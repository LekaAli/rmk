from django import forms


class CapacityRampUpForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    rampup_type = forms.CharField(widget=forms.Select)
    rampup_values = forms.CharField(widget=forms.SelectMultiple)
    year = forms.CharField()
    will_roll_over = forms.BooleanField()
    
    name.widget.attrs['placeholder'] = 'Ramp Up Description'


class CapacityRampUpValuesForm(forms.Form):
    month = forms.CharField(widget=forms.Select)
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'
