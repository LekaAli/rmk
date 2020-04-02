from django import forms
from .models import Product, Expense
from rampup.models import RampUp
from seasonality.models import Seasonality
from rmkplatform.constants import MONTHS
from dates.models import FinancialYear


class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    MONTH = [(-1, '---Select Projection Month---')]
    MONTHS = [MONTHS[i] for i in range(len(MONTHS)) if i != 0]
    MONTH.extend(MONTHS)
    projection_start = forms.CharField(widget=forms.Select(choices=MONTH), required=True, initial='-1')
    average_unit_price = forms.DecimalField()
    average_quantity_per_month = forms.IntegerField()
    
    name.widget.attrs['placeholder'] = 'Product Description'
    average_unit_price.widget.attrs['placeholder'] = 'Unit Price'
    average_quantity_per_month.widget.attrs['placeholder'] = 'Quantity Per Month'


class AddNProductForm(forms.Form):
    product_count = forms.CharField(widget=forms.TextInput)
    
    product_count.widget.attrs['placeholder'] = 'Add How Many Product(s)'
    
    
class ProductEditForm(forms.Form):
    PRODUCT = [(-1, '---Select Product---')]
    try:
        PRODUCT.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    name = forms.CharField(widget=forms.Select(choices=PRODUCT), required=True, initial='-1')


class CostOfSaleForm(forms.Form):

    # description = forms.CharField(widget=forms.TextInput)
    products = [(-1, '---Select Product---')]
    try:
        products.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        products = []
    product = forms.CharField(widget=forms.Select(choices=products))
    percentage = forms.CharField(widget=forms.TextInput)
    
    # description.widget.attrs['placeholder'] = 'Cost Of Sale Description'
    product.widget.attrs['placeholder'] = 'Cost Of Sale Product'
    percentage.widget.attrs['placeholder'] = 'Cost Of Sale Value'


class CostOfSaleEditForm(forms.Form):
    products = [(-1, '---Select Product---')]
    try:
        products.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        products = []
    product = forms.CharField(widget=forms.Select(choices=products))


class AddNExpenseForm(forms.Form):
    expense_count = forms.CharField(widget=forms.TextInput)
    
    expense_count.widget.attrs['placeholder'] = 'How Many Expense(s)'
    
    
class ExpenseForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput)
    is_fixed = forms.CharField(widget=forms.Select(choices=[(0, '---Select Expense Type---'), (1, 'Fixed'), (0, 'Not Fixed')]), initial='0', required=True)
    value = forms.DecimalField()

    description.widget.attrs['placeholder'] = 'Expense Description'
    value.widget.attrs['placeholder'] = 'Expense Value'


class ExpenseEditForm(forms.Form):
    EXPENSES = [('-1', '---Select Expense---')]
    try:
        EXPENSES.extend(list(Expense.objects.values_list('id', 'description')))
    except Exception as ex:
        pass
    description = forms.CharField(widget=forms.Select(choices=EXPENSES), initial='-1')
    
    
class ProductSeasonalityRampUpAssignment(forms.Form):
    products = [(-1, '---Select Product---')]
    try:
        products.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass

    seasonality = [(-1, '---Select Product Seasonality---')]
    try:
        seasonality.extend(list(Seasonality.objects.values_list('id', 'name')))
    except Exception as ex:
        pass

    rampup = [(-1, '---Select Product Ramp Up---')]
    try:
        rampup.extend(list(RampUp.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    product = forms.CharField(widget=forms.Select(choices=products), initial='-1', required=True)
    seasonality = forms.CharField(widget=forms.Select(choices=seasonality), initial='-1', required=True)
    rampup = forms.CharField(widget=forms.Select(choices=rampup), initial='-1', required=True)


class ProductAssignmentEditForm(forms.Form):
    products = [(-1, '---Select Product---')]
    try:
        products.extend(list(Product.objects.values_list('id', 'name')))
    except Exception as ex:
        pass
    product = forms.CharField(widget=forms.Select(choices=products), initial='-1', required=True)
    

class TaxForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(list(FinancialYear.objects.values_list('id', 'description')))
    except Exception as ex:
        pass
    financial_year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1', required=True)
    tax_percentage = forms.FloatField()
    tax_percentage.widget.attrs['placeholder'] = 'Tax Percentage Value'
    
    
class TaxEditForm(forms.Form):
    YEARS = [(-1, '---Select Financial Year---')]
    try:
        YEARS.extend(list(FinancialYear.objects.values_list('id', 'description')))
    except Exception as ex:
        pass
    financial_year = forms.CharField(widget=forms.Select(choices=YEARS), initial='-1', required=True)
