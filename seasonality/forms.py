from django import forms
from rmkplatform.constants import MONTHS, TYPE


class SeasonalityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    seasonality_type = forms.ChoiceField(widget=forms.Select(), choices=TYPE, initial='-1')
    seasonality_values = forms.CharField(widget=forms.SelectMultiple)
    year = forms.CharField(widget=forms.Select)
    will_roll_over = forms.BooleanField()
    
    name.widget.attrs['placeholder'] = 'Seasonality Description'


class SeasonalityValuesForm(forms.Form):
    month = forms.ChoiceField(widget=forms.Select(), choices=MONTHS, initial='0', show_hidden_initial=True)
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Seasonality Percentage Value'
