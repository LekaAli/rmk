from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from .forms import CapacityRampUpForm, CapacityRampUpValuesForm, CapacityRampUpValuesUpdateForm, CapacityRampUpValuesEditForm, CapacityRampUpEditForm
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
                    return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': '', 'action': 'add'})
                rampup_instance = RampUp(**data)
                rampup_instance.save()
                if len(vals) > 0:
                    rampup_instance.rampup_values.add(*vals)
                    rampup_instance.save()
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpForm()
    return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'add'})


def edit_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_instance = RampUp.objects.get(id=data.get('name'))
                form = CapacityRampUpForm({
                    'name': rampup_instance.name,
                    'rampup_type': rampup_instance.rampup_type,
                    'rampup_values': list(rampup_instance.rampup_values.values_list('id')),
                    'year': rampup_instance.year.id,
                    'will_roll_over': rampup_instance.will_roll_over
                })
            except Exception as ex:
                form = CapacityRampUpEditForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'update'})
    else:
        form = CapacityRampUpEditForm()
    return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'edit'})


def update_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_instance = RampUp.objects.get(name__iexact=data.get('name'))
                rampup_instance.rampup_type = data.get('rampup_type')
                rampup_instance.rampup_values.set(data.get('rampup_values'))
                rampup_instance.year.id = data.get('year')
                rampup_instance.will_roll_over = data.get('will_roll_over')
                rampup_instance.save()
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Ramp Up', 'message': 'Ramp Up Successfully Updated'})
    else:
        form = CapacityRampUpForm()
    return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'add'})


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
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up Value', 'message': 'Ramp Up Successfully Added'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'add'})


def edit_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instance = RampUpValue.objects.get(**data)
                form = CapacityRampUpValuesForm({
                    'month': rampup_value_instance.month,
                    'percentage': rampup_value_instance.percentage
                })
            except Exception as ex:
                form = CapacityRampUpValuesEditForm()
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex})
            return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'update'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'edit'})


def update_rampup_value(request):
    if request.method == 'POST':
        form = CapacityRampUpValuesUpdateForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instance = RampUpValue.objects.get(**{'month': data.get('month', 0)})
                rampup_value_instance.percentage = data.get('percentage')
                rampup_value_instance.save()
            except Exception as ex:
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Ramp Up Value', 'message': 'Ramp Up Value Successfully Updated'})
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'action': 'edit'})
