from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Inflation
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas



# Create your views here.
class InflationInput(CreateView):
    model = Inflation
    template_name = 'inflation/inflation.html'
    
    fields = '__all__'