from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from revenues.models import ProductRevenue
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from .import forms

# Create your views here.


class RevenueInput(CreateView):
    model = ProductRevenue
    template_name = 'revenues/revenue.html'
    
    fields = '__all__'

