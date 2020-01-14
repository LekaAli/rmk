from django import forms
from .models import FinancialYear


class DatesForm(forms.Form):
    description = forms.CharField()
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
    years = [(-1, '---Select Financial Year---')]
    years.extend(list(FinancialYear.objects.values_list('id', 'description')))
    description = forms.CharField(widget=forms.Select(choices=years), initial='-1', required=True)


