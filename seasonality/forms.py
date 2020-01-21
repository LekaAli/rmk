from django import forms
from dates.models import FinancialYear
from .models import SeasonalityValue
from rmkplatform.constants import TYPE, MONTHS


class SeasonalityForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(list(FinancialYear.objects.values_list('id', 'description')))
        VALUES = SeasonalityValue.objects.all()
        V = [(val.id, '%s - %s' % (val.month_name, val.percentage)) for val in VALUES]
    except Exception as ex:
        YEARS = []
        V = []
    name = forms.CharField()
    seasonality_type = forms.CharField(widget=forms.Select(choices=TYPE))
    seasonality_values = forms.MultipleChoiceField(choices=V, widget=forms.SelectMultiple(), required=False)
    year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1', required=True)
    will_roll_over = forms.BooleanField(required=False)
    
    name.widget.attrs['placeholder'] = 'Seasonality Description'
    will_roll_over.widget.attrs['style'] = 'width:20px'


class SeasonalityValuesForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), required=True, initial='-1')
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Seasonality Percentage Value'


class SeasonalityValuesEditForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), required=True, initial='-1')

