from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Dates, FinancialYear
from .import forms
from django.urls import reverse
from django.views import generic
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas


class CreateDates1(CreateView):
    model = FinancialYear
    template_name = 'dates/dates_form.html'
    fields = ['description', 'start_date', 'inflation']


def create_dates(request):
    if request.method == 'POST':
        form = forms.DatesForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = forms.DatesForm()
    return render(request, 'dates/dates_form.html', {'form': form})

