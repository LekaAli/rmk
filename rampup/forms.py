from django import forms
from .models import RampUpValue, RampUp
from dates.models import FinancialYear
from rmkplatform.constants import TYPE, MONTHS


class CapacityRampUpForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(list(FinancialYear.objects.values_list('id', 'description')))
        VALUES = RampUpValue.objects.all()
        V = [(val.id, '%s - %s' % (val.month_name, val.percentage)) for val in VALUES]
    except Exception as ex:
        V = []
        YEARS = []
    
    name = forms.CharField(widget=forms.TextInput)
    rampup_type = forms.CharField(widget=forms.Select(choices=TYPE), initial='-1', required=True)
    rampup_values = forms.MultipleChoiceField(choices=V, widget=forms.SelectMultiple(), required=False)
    year = forms.ChoiceField(widget=forms.Select(), choices=YEARS, initial='-1', required=True)
    will_roll_over = forms.BooleanField(required=False)
    
    name.widget.attrs['placeholder'] = 'Ramp Up Description'
    will_roll_over.widget.attrs['style'] = 'width:20px'


class CapacityRampUpEditForm(forms.Form):
    RAMPUP = [(-1, '---Select RampUp---')]
    try:
        RAMPUP.extend(list(RampUp.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    name = forms.CharField(widget=forms.Select(choices=RAMPUP), initial='-1')


class CapacityRampUpValuesForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)
    percentage = forms.CharField(widget=forms.TextInput, required=True)
    
    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'


class CapacityRampUpValuesEditForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)


class CapacityRampUpValuesUpdateForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)
    percentage = forms.CharField(widget=forms.TextInput, required=True)

    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'
