from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from .forms import CapacityRampUpForm, CapacityRampUpValuesForm, CapacityRampUpValuesUpdateForm, CapacityRampUpValuesEditForm, CapacityRampUpEditForm
from dates.models import FinancialYear
from .models import RampUp, RampUpValue
from rmkplatform.constants import MONTHS


def add_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                year_instance = FinancialYear.objects.filter(id=data['year'])
                if year_instance.count() > 0:
                    year = year_instance.first()
                    months = dict()
                    start = year.start_date.month
                    for year_value in range(year.start_date.year, year.end_date.year + 1):
                        months.update({year_value: list()})
                        for month in range(start, 12 + 1):
                            months[year_value].append(month)
                            if year_value == year.end_date.year and (month % 12) == year.end_date.month:
                                break
                        start = 1
                    month = {entry[0]: entry[1] for entry in MONTHS[2:]}
                    month_lst = list()
                    for year_id, month_ids in months.items():
                        for month_id in month_ids:
                            month_lst.append([month_id, '%s %s' % (month.get(month_id), year_id)])
                else:
                    form = CapacityRampUpForm()
                    return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': '', 'action': 'add'})
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html',
                              {'form': form, 'action': 'add', 'months': month_lst, 'year': data['year']})
                # rampup_instance = RampUp(**data)
                # rampup_instance.save()
                # if len(vals) > 0:
                #     rampup_instance.rampup_values.add(*vals)
                #     rampup_instance.save()
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'add'})
            # return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up', 'message': 'Ramp Up Successfully Added'})
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
        request_data = dict(request.POST)
        data = {'month': request_data.get('month'), 'percentage': request_data.get('percentage'), 'year': request_data.get('year')[0]}
        form_data = dict()
        for month_index, month_value in enumerate(data.get('month')):
            form_data.update({'month': month_value, 'percentage': data['percentage'][month_index], 'financial_year': data['year']})
            form = CapacityRampUpValuesForm(form_data)
            if form.is_valid():
                try:
                    data = form.cleaned_data
                    rampup_value_instance = RampUpValue(**data)
                    rampup_value_instance.save()
                except Exception as ex:
                    form = CapacityRampUpValuesForm()
                    return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': ex, 'action': 'add'})
                return render(request, 'dates/success.html', {'btn_name': 'Add Another Ramp Up Value', 'view': 'rampup', 'message': 'Ramp Up Successfully Added'})
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
