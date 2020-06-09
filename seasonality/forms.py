from django import forms
from dates.models import FinancialYear
from .models import Seasonality
from products.models import Product
from rmkplatform.constants import TYPE, MONTHS


class SeasonalityForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---'), (0, 'All')]
    try:
        YEARS.extend(list(FinancialYear.objects.filter(description__in=['Year 1', 'Year 2']).values_list('id', 'description')))
    except Exception as ex:
        pass
        
    try:
        if len(TYPE) > 2:
            TYPE = TYPE[:2]
        TYPE.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
        
    seasonality_type = forms.CharField(widget=forms.Select(choices=TYPE), initial='-1', required=True)
    year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1', required=True)


class SeasonalityEditForm(forms.Form):
    SEASONALITY = [(-1, '---Select Seasonality---')]
    try:
        SEASONALITY.extend(list(Seasonality.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    name = forms.CharField(widget=forms.Select(choices=SEASONALITY), initial='-1')

    
class SeasonalityValuesForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(
            list(FinancialYear.objects.filter(description__in=['Year 1', 'Year 2']).values_list('id', 'description')))
        YEARS.append(('-2', 'All'))
    except Exception as ex:
        pass
    try:
        products = Product.objects.values_list('id', 'name')
        TYPE.extend(products)
    except Exception as ex:
        TYPE = []
    financial_year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1', required=True)
    month = forms.CharField(widget=forms.Select(choices=MONTHS), required=True, initial='-1')
    percentage = forms.CharField(widget=forms.TextInput)
    product = forms.MultipleChoiceField(choices=TYPE, widget=forms.SelectMultiple(), required=False)
    percentage.widget.attrs['placeholder'] = 'Seasonality Percentage Value'


class SeasonalityValuesEditForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), required=True, initial='-1')

