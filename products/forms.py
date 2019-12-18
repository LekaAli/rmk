from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    projection_start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'}))
    average_unit_price = forms.DecimalField()
    average_quantity_per_month = forms.IntegerField()
    
    name.widget.attrs['placeholder'] = 'Product Description'
    average_unit_price.widget.attrs['placeholder'] = 'Unit Price'
    average_quantity_per_month.widget.attrs['placeholder'] = 'Quantity Per Month'


class CostOfSaleForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput)
    product = forms.CharField(widget=forms.Select)
    percentage = forms.CharField(widget=forms.TextInput)
    
    description.widget.attrs['placeholder'] = 'Cost Of Sale Description'
    product.widget.attrs['placeholder'] = 'Cost Of Sale Product'
    percentage.widget.attrs['placeholder'] = 'Cost Of Sale Value'


class ExpenseForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput)
    is_fixed = forms.BooleanField()
    value = forms.DecimalField()

    description.widget.attrs['placeholder'] = 'Expense Description'
    value.widget.attrs['placeholder'] = 'Expense Value'
