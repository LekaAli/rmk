from django import forms
from dates.date_utils import years, filter_dates
from dates.models import FinancialYear

    
class DatesForm(forms.Form):
    
    description = forms.CharField(widget=forms.Select(choices=[('1', 'Year 1')]), initial='1', required=True)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "mm/dd/yyyy"
            }
        ))
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "mm/dd/yyyy"
            }
        ))
    inflation = forms.FloatField()

    description.widget.attrs['placeholder'] = 'Year Description'
    inflation.widget.attrs['placeholder'] = 'Inflation Value'


class AdvancedDatesForm(forms.Form):
    year_counts = forms.IntegerField()
    year_counts.widget.attrs['placeholder'] = 'How Many Financial Years?'
    
    
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