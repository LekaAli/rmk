from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Dates
from .import forms
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas



# Create your views here.


class CreateDates(CreateView):
    model = Dates
    template_name = 'dates/dates_form.html'
    
    fields = '__all__'


# Create your views here.
