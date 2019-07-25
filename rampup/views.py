from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from rampup.models import CapacityRampUp
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from .import forms

# Create your views here.


class RampUpInput(CreateView):
    model = CapacityRampUp
    template_name = 'rampup/capacity_ramp_up.html'
    
    fields = '__all__'
