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