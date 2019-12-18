from django import forms
from .models import RampUpValue
from dates.models import FinancialYear


class CapacityRampUpForm(forms.Form):
    TYPE = (
        (0, 'For Many Products'),
        (1, 'For One Product')
    )
    YEARS = FinancialYear.objects.values_list('id', 'description')
    VALUES = RampUpValue.objects.all()
    V = [(val.id, '%s - %s' % (val.month_name, val.percentage)) for val in VALUES]
    name = forms.CharField(widget=forms.TextInput)
    rampup_type = forms.CharField(widget=forms.Select(choices=TYPE))
    rampup_values = forms.MultipleChoiceField(choices=V, widget=forms.SelectMultiple(), required=False)
    year = forms.CharField(widget=forms.Select(choices=YEARS))
    will_roll_over = forms.BooleanField(required=False)
    
    name.widget.attrs['placeholder'] = 'Ramp Up Description'
    will_roll_over.widget.attrs['style'] = 'width:20px'


class CapacityRampUpValuesForm(forms.Form):
    VALUES = RampUpValue.objects.all()
    MONTHS = [(val.id, '%s' % val.month_name) for val in VALUES]
    month = forms.CharField(widget=forms.Select(choices=MONTHS))
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'
