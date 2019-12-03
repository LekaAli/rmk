
from django import forms
from .import models


class DatesForm1(forms.ModelForm):
    class Meta:
        model = models.FinancialYear
        fields = '__all__'
        
        
class DatesForm(forms.Form):
    description = forms.CharField(label='Description', max_length=50)
    start_date = forms.DateField(label='Start Date')
    inflation = forms.DecimalField(label='Inflation Value')
