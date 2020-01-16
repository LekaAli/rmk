from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from .forms import CapacityRampUpForm, CapacityRampUpValuesForm
from dates.models import FinancialYear
from .models import RampUp, RampUpValue


def add_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                vals = data.pop('rampup_values')
                year_instance = FinancialYear.objects.filter(id=data['year'])
                if year_instance.count() > 0:
                    data['year'] = year_instance[0]
                else:
                    form = CapacityRampUpForm()
                    return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ''})
                rampup_instance = RampUp(**data)
                rampup_instance.save()
                if len(vals) > 0:
                    rampup_instance.rampup_values.add(*vals)
                    rampup_instance.save()
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpForm()
    return render(request, 'rampup/add_rampup.html', {'form': form})


def add_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instance = RampUpValue(**data)
                rampup_value_instance.save()
            except Exception as ex:
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up Value', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'add'})


def edit_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instance = RampUpValue(**data)
                rampup_value_instance.save()
            except Exception as ex:
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up Value', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'edit'})


def update_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instance = RampUpValue(**data)
                rampup_value_instance.save()
            except Exception as ex:
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up Value', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'edit'})
