from django import forms
from .models import RampUpValue, RampUp
from dates.models import FinancialYear
from products.models import Product
from rmkplatform.constants import TYPE, MONTHS


class CapacityRampUpForm(forms.Form):
    
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(list(FinancialYear.objects.filter(description__in=['Year 1', 'Year 2']).values_list('id', 'description')))
        YEARS.append(('-2', 'All'))
        VALUES = RampUpValue.objects.all()
        V = [(val.id, '%s - %s' % (val.month, val.percentage)) for val in VALUES]
    except Exception as ex:
        V = []
    try:
        products = Product.objects.all().values_list('id', 'name')
        TYPE.extend(products)
    except Exception as ex:
        TYPE = []

    rampup_type = forms.CharField(widget=forms.Select(choices=TYPE), initial='-1', required=True)
    year = forms.ChoiceField(widget=forms.Select(), choices=YEARS, initial='-1', required=True)
    will_roll_over = forms.BooleanField(required=False)

    will_roll_over.widget.attrs['style'] = 'width:20px'


class CapacityRampUpEditForm(forms.Form):
    RAMPUP = [(-1, '---Select RampUp---')]
    try:
        RAMPUP.extend(list(RampUp.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    name = forms.CharField(widget=forms.Select(choices=RAMPUP), initial='-1')


class CapacityRampUpValuesForm(forms.Form):
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
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)
    percentage = forms.CharField(widget=forms.TextInput, required=True)
    product = forms.MultipleChoiceField(choices=TYPE, widget=forms.SelectMultiple(), required=False)
    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'


class CapacityRampUpValuesEditForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)


class CapacityRampUpValuesUpdateForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1', required=True)
    percentage = forms.CharField(widget=forms.TextInput, required=True)

    percentage.widget.attrs['placeholder'] = 'Ramp Up Percentage Value'
