from django import forms
from revenues.models import Revenue

class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = '__all__'
