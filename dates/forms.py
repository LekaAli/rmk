from django import forms
from dates.date_utils import years, filter_dates

    
class DatesForm(forms.Form):
    
    description = forms.CharField(widget=forms.Select(choices=filter_dates(years)), initial='-1', required=True)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "mm/dd/yyyy"
            }
        ))
    inflation = forms.FloatField()
    year_counts = forms.IntegerField()

    description.widget.attrs['placeholder'] = 'Year Description'
    inflation.widget.attrs['placeholder'] = 'Inflation Value'
    year_counts.widget.attrs['placeholder'] = 'Financial Year Count'
    
    
class EditDates(forms.Form):
    
    description = forms.CharField(widget=forms.Select(choices=years), initial='-1', required=True)


class UpdateForm(forms.Form):
    description = forms.CharField()
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "mm/dd/yyyy"
            }
        ))
    inflation = forms.FloatField()

    description.widget.attrs['placeholder'] = 'Year Description'
    inflation.widget.attrs['placeholder'] = 'Inflation Value'