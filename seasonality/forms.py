from django import forms


class SeasonalityForm(forms.Form):
    name = forms.CharField(widget=forms.Select)
    seasonality_type = forms.CharField(widget=forms.Select)
    seasonality_values = forms.CharField(widget=forms.SelectMultiple)
    year = forms.CharField(widget=forms.Select)
    will_roll_over = forms.BooleanField()
    
    name.widget.attrs['placeholder'] = 'Seasonality Description'


class SeasonalityValuesForm(forms.Form):
    month = forms.CharField(widget=forms.Select)
    percentage = forms.CharField(widget=forms.TextInput)
    
    percentage.widget.attrs['placeholder'] = 'Seasonality Percentage Value'
