from django import forms
from revenues.models import Revenue
from products.models import Product
from dates.date_utils import years
from rmkplatform.constants import MONTHS


class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = '__all__'
        

class GenerateRevenuePrediction(forms.Form):
    PRODUCTS = [(-1, '---Select Product---'), (0, 'All')]
    MONTH = [(-1, '---Select Month---')]
    
    try:
        PRODUCTS.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    
    product = forms.CharField(widget=forms.Select(choices=PRODUCTS), initial='-1')
    year = forms.CharField(widget=forms.Select(choices=years), initial='-1')
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1')
    tax = forms.CharField(widget=forms.TextInput, required=False)

    tax.widget.attrs['placeholder'] = 'Tax Percentage'
    
    product.default_error_messages['required'] = 'Product is Required.'
    year.default_error_messages['required'] = 'Financial Year is Required.'
    month.default_error_messages['required'] = 'Month is Required.'
    tax.default_error_messages['required'] = 'Tax value is Required.'
