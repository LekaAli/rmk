from django import forms
from .import models

class BusinessForm(forms.ModelForm):
    class Meta:
        model = models.BusinessDetails
        fields = '__all__'
    

class PromoterForm(forms.ModelForm):
    class Meta:
        model = models.Promoter
        fields = '__all__'
        widgets = {'gender': forms.RadioSelect}

    