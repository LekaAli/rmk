from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from seasonality.models import SeasonalityValue
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO


# Create your views here.
class SeasonalityInput(CreateView):
    model = SeasonalityValue
    template_name = 'seasonality/product_seasonality.html'
    
    fields = '__all__'