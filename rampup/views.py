from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, render, reverse
from .forms import CapacityRampUpForm, CapacityRampUpValuesForm, CapacityRampUpValuesUpdateForm, CapacityRampUpValuesEditForm, CapacityRampUpEditForm
from dates.models import FinancialYear
from .models import RampUp, RampUpValue
from products.models import Product
from rmkplatform.constants import MONTHS


def monthly_breakdown(f_year_instance):
    months = dict()
    start = f_year_instance.start_date.month
    for year_value in range(f_year_instance.start_date.year, f_year_instance.end_date.year + 1):
        months.update({year_value: list()})
        for month in range(start, 12 + 1):
            months[year_value].append(month)
            if year_value == f_year_instance.end_date.year and (month % 12) == f_year_instance.end_date.month:
                break
        start = 1
    month = {entry[0]: entry[1] for entry in MONTHS[2:]}
    month_lst = list()
    for year_id, month_ids in months.items():
        for month_id in month_ids:
            month_lst.append([month_id, '%s %s' % (month.get(month_id), year_id)])
    return month_lst


def cal_num_of_months(end_date, start_date):
    return abs((end_date.year - start_date.year) * 12 + end_date.month - start_date.month) + 1


def add_rampup(request):
    if request.method == 'POST':
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                if data['year'] in ['-2', -2]:
                    year_instance = FinancialYear.objects.filter(description__in=['Year 1', 'Year 2'])
                else:
                    year_instance = FinancialYear.objects.filter(id=data['year'])
                    
                if data['rampup_type'] in ['0', 0]:
                    product = list(Product.objects.values_list('id', flat=True))
                else:
                    product = list(Product.objects.filter(id=int(data['rampup_type'])).values_list('id', flat=True))
                values_dict = dict()
                if year_instance.count() > 0:
                    for year in year_instance:
                        values_dict.update({year.description: monthly_breakdown(year)})
                else:
                    form = CapacityRampUpForm()
                    return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': '', 'action': 'add'})
                form = CapacityRampUpValuesForm()
                return render(request, 'rampup/add_rampup_values.html',
                              {'form': form, 'action': 'add', 'values': values_dict, 'product': ','.join([str(i) for i in product]), 'year': ','.join(values_dict.keys())})
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'add'})
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
        data = {
            'month': request_data.get('month'),
            'percentage': request_data.get('percentage'),
            'financial_year': request_data.get('year')[0].split(','),
            'product': request_data.get('product')[0].split(',')
        }
        form_data = dict()
        errors = list()
        for year in data.get('financial_year'):
            f_year = FinancialYear.objects.get(description=year)
            num_of_month = cal_num_of_months(f_year.end_date, f_year.start_date)
                
            percentages = data['percentage'][:num_of_month] if year == 'Year 1' else data['percentage'][num_of_month:]
            months = data.get('month')[:num_of_month] if year == 'Year 1' else data.get('month')[num_of_month:]
            for month_index, month_value in enumerate(months):
                form_data.update({
                    'financial_year': year,
                    'month': month_value,
                    'percentage': percentages[month_index]
                })
                query = QueryDict('', mutable=True)
                query.update(form_data)
                form = CapacityRampUpValuesForm(query)
                if form.is_valid():
                    try:
                        clean_data = form.cleaned_data
                        f_year = FinancialYear.objects.get(description=clean_data.get('financial_year'))
                        clean_data['financial_year'] = f_year
                        product_ids = [int(val) for val in data.get('product')]
                        clean_data.pop('product')
                        rampup_value_instance = RampUpValue(**clean_data)
                        rampup_value_instance.save()
                        rampup_value_instance.product.set(product_ids)
                    except Exception as ex:
                        errors.append(ex)
        if errors:
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
