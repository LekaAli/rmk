from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SeasonalityForm, SeasonalityValuesForm


def add_seaasonality(request):
    if request.method == 'POST':
        form = SeasonalityForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = SeasonalityForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form})


def add_seasonality_value(request):
    if request.method == 'POST':
        form = SeasonalityValuesForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality_values.html', {'form': form})