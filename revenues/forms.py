from django import forms
from revenues.models import Revenue
from products.models import Product
from dates.models import FinancialYear
from rmkplatform.constants import MONTHS

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = '__all__'
        
        
class GenerateRevenuePrediction(forms.Form):
    PRODUCTS = [(-1, '---Select Product---'), (0, 'All')]
    YEARS = [(-1, '---Select Financial Year---')]
    MONTH = [(-1, '---Select Month---')]
    # MONTH.extend(MONTHS)
    
    try:
        PRODUCTS.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    
    try:
        YEARS.extend(list(FinancialYear.objects.values_list('id', 'description')))
    except Exception as ex:
        pass
    
    product = forms.CharField(widget=forms.Select(choices=PRODUCTS), initial='-1')
    year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1')
    month = forms.CharField(widget=forms.Select(choices=MONTHS), initial='-1')
    
    product.default_error_messages['required'] = 'Product is Required.'
    year.default_error_messages['required'] = 'Financial Year is Required.'
    month.default_error_messages['required'] = 'Month is Required.'
