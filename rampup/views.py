from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from .forms import CapacityRampUpForm, CapacityRampUpValuesForm


def add_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = CapacityRampUpForm()
    return render(request, 'rampup/add_rampup.html', {'form': form})


def add_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form})
