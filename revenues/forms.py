from django import forms
from revenues.models import ProductRevenue

class RevenueForm(forms.ModelForm):
    class Meta:
        model = ProductRevenue
        fields = '__all__'
