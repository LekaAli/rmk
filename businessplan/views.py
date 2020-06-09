from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import BusinessDetails, Promoter
from .import forms
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas



# Create your views here.


class BusinessInfo(CreateView):
    model = BusinessDetails
    template_name = 'businessplan/business_details.html'
    
    fields = '__all__'

class PromoterCreator(CreateView):
    model = Promoter
    template_name = 'businessplan/promoter_form.html'
    
    fields = '__all__'
    

