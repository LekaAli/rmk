from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, render, reverse

from dates.views import already_created_dates
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
    is_loaded = already_created_dates('rampup', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Update',
            'view': 'rampup',
            'action': 'review',
            'message': 'Ramp Up Options'
        })
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
        form = CapacityRampUpForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                rampup_value_instances = RampUpValue.objects.filter(
                    financial_year=data['year'],
                    product=data['rampup_type']
                ).values_list('id', 'financial_year__description', 'month', 'percentage', 'product__name')
                
            except Exception as ex:
                form = CapacityRampUpForm()
                return render(request, 'rampup/add_rampup.html', {'form': form, 'errors': ex, 'action': 'edit'})
            if len(rampup_value_instances) == 0:
                form = CapacityRampUpForm()
                return render(
                    request, 
                    'rampup/add_rampup.html',
                    {'form': form, 'action': 'edit', 'message': 'No matching record(s) found'}
                )
            form = CapacityRampUpValuesForm()
            return render(
                request,
                'rampup/add_rampup.html',
                {
                    'form': form,
                    'action': 'update',
                    'values': enumerate(rampup_value_instances),
                    'year': rampup_value_instances[0][1]
                }
            )
    else:
        form = CapacityRampUpForm()
    return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'edit'})


def update_rampup(request):
    if request.method == 'POST':
        request_data = dict(request.POST)
        data = {
            'month': request_data.get('month'),
            'percentage': request_data.get('percentage'),
            'financial_year': list(set(request_data.get('financial_year'))),
            'product': list(set(request_data.get('product')))
        }
        errors = False
        for year in data.get('financial_year'):
            f_year = FinancialYear.objects.get(description=year)
            for product_name in data.get('product'):
                try:
                    for item_index, month_val in enumerate(data.get('month')):
                        month_percent_val = data.get('percentage')[item_index]
                        ramp_up_instance = RampUpValue.objects.filter(financial_year=f_year, month=month_val, product__name=product_name)
                        ramp_up = ramp_up_instance.first()
                        if ramp_up.percentage != float(month_percent_val):
                            ramp_up.percentage = month_percent_val
                            ramp_up.save()
                except Exception as ex:
                    errors = True
                    break
            if errors is True:
                break
        if errors is True:
            rampup_value_instances = RampUpValue.objects.filter(
                financial_year__description__in=request_data.get('financial_year'),
                product__name__in=list(set(request_data.get('product')))
            ).values_list('id', 'financial_year__description', 'month', 'percentage', 'product__name')
            form = CapacityRampUpValuesForm()
            return render(
                request,
                'rampup/add_rampup.html',
                {
                    'form': form,
                    'action': 'update',
                    'values': enumerate(rampup_value_instances),
                    'year': rampup_value_instances[0][1]
                }
            )
        return render(
            request,
            'dates/success.html',
            {'btn_name': 'Update', 'view': 'rampup', 'action': 'review', 'message': 'Ramp Up Successfully Updated'}
        )
    else:
        form = CapacityRampUpValuesForm()
    return render(request, 'rampup/add_rampup.html', {'form': form, 'action': 'add'})


def view_rampup_value(request):
    rampups = RampUpValue.objects.all().order_by('id').values_list('financial_year__description', 'month', 'percentage', 'product__name')
    print(rampups)
    return render(request, 'rampup/view_rampup.html', context={'data': enumerate(rampups)})


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
            product_ids = [int(val) for val in data.get('product')]
            RampUpValue.objects.filter(product__in=product_ids, financial_year=f_year).delete()
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
                        clean_data.pop('product')
                        rampup_value_instance = RampUpValue(**clean_data)
                        rampup_value_instance.save()
                        rampup_value_instance.product.set(product_ids)
                    except Exception as ex:
                        errors.append(ex)
        if errors:
            form = CapacityRampUpValuesForm()
            return render(request, 'rampup/add_rampup_values.html', {'form': form, 'errors': errors, 'action': 'add'})
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
