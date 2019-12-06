from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import FinancialYear
from .import forms
from django.urls import reverse


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

