from django.http import QueryDict
from django.shortcuts import render

from dates.views import already_created_dates
from products.models import Product
from rampup.views import monthly_breakdown, cal_num_of_months
from .forms import SeasonalityForm, SeasonalityValuesForm, SeasonalityValuesEditForm, SeasonalityEditForm
from .models import Seasonality, SeasonalityValue
from dates.models import FinancialYear


def add_seasonality(request):
    is_loaded = already_created_dates('seasonality', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Update',
            'view': 'seasonality',
            'action': 'review',
            'message': 'Seasonality Options'
        })
    if request.method == 'POST':
        form = SeasonalityForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                if data['year'] in ['0', 0]:
                    year_instance = FinancialYear.objects.filter(description__in=['Year 1', 'Year 2'])
                else:
                    year_instance = FinancialYear.objects.filter(id=data['year'])
                    
                if data['seasonality_type'] in ['0', 0]:
                    product = list(Product.objects.values_list('id', flat=True))
                else:
                    product = list(Product.objects.filter(id=int(data['seasonality_type'])).values_list('id', flat=True))
                values_dict = dict()
                if year_instance.count() > 0:
                    for year in year_instance:
                        values_dict.update({year.description: monthly_breakdown(year)})
                else:
                    form = SeasonalityForm()
                    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'add'})
                form = SeasonalityValuesForm()
                return render(request, 'seasonality/add_seasonality_values.html',
                              {'form': form, 'action': 'add', 'values': values_dict,
                               'product': ','.join([str(i) for i in product]), 'year': ','.join(values_dict.keys())})
            except Exception as ex:
                form = SeasonalityForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex, 'action': 'add'})
    else:
        form = SeasonalityForm()
        return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'add'})


def edit_seasonality(request):
    if request.method == 'POST':
        form = SeasonalityForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_value_instances = SeasonalityValue.objects.filter(
                    financial_year=data['year'],
                    product=data['seasonality_type']
                ).values_list('id', 'financial_year__description', 'month', 'percentage', 'product__name')
            
            except Exception as ex:
                form = SeasonalityForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex, 'action': 'edit'})
            if len(seasonality_value_instances) == 0:
                form = SeasonalityForm()
                return render(
                    request,
                    'seasonality/product_seasonality.html',
                    {'form': form, 'action': 'edit', 'message': 'No matching record(s) found'}
                )
            form = SeasonalityValuesForm()
            return render(
                request,
                'seasonality/product_seasonality.html',
                {
                    'form': form,
                    'action': 'update',
                    'values': enumerate(seasonality_value_instances),
                    'year': seasonality_value_instances[0][1]
                }
            )
    else:
        form = SeasonalityForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'edit'})


def update_seasonality(request):
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
                        ramp_up_instance = SeasonalityValue.objects.filter(financial_year=f_year, month=month_val,
                                                                      product__name=product_name)
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
            rampup_value_instances = SeasonalityValue.objects.filter(
                financial_year__description__in=request_data.get('financial_year'),
                product__name__in=list(set(request_data.get('product')))
            ).values_list('id', 'financial_year__description', 'month', 'percentage', 'product__name')
            form = SeasonalityValuesForm()
            return render(
                request,
                'seasonality/product_seasonality.html',
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
            {'btn_name': 'Update', 'view': 'seasonality', 'action': 'review', 'message': 'Seasonality Successfully Updated'}
        )
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'add'})


def edit_seasonality_value(request):
    if request.method == 'POST':
        form = SeasonalityValuesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_value_instance = SeasonalityValue(**data)
                seasonality_value_instance.save()
            except Exception as ex:
                form = SeasonalityValuesForm()
                return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Seasonality Value', 'message': 'Seasonality Value Successfully Added', 'action': 'add'})
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'action': 'add'})


def view_seasonality_value(request):
    seasonalities = SeasonalityValue.objects.all().order_by('id').values_list(
        'financial_year__description',
        'month',
        'percentage',
        'product__name'
    )
    return render(request, 'seasonality/view_seasonality.html', context={'data': enumerate(seasonalities)})


def add_seasonality_value(request):
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
                form = SeasonalityValuesForm(query)
                if form.is_valid():
                    try:
                        clean_data = form.cleaned_data
                        f_year = FinancialYear.objects.get(description=clean_data.get('financial_year'))
                        clean_data['financial_year'] = f_year
                        product_ids = [int(val) for val in data.get('product')]
                        clean_data.pop('product')
                        rampup_value_instance = SeasonalityValue(**clean_data)
                        rampup_value_instance.save()
                        rampup_value_instance.product.set(product_ids)
                    except Exception as ex:
                        errors.append(ex)
        if errors:
            form = SeasonalityValuesForm()
            return render(request, 'seasonality/add_seasonality_values.html', {'form': form, 'errors': errors, 'action': 'add'})
        return render(request, 'dates/success.html', {'btn_name': 'Add Another Seasonality Value', 'view': 'seasonality',
                                                      'message': 'Seasonality Successfully Added'})
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'action': 'edit'})


def update_seasonality_value(request):
    if request.method == 'POST':
        form = SeasonalityValuesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_value_instance = SeasonalityValue.objects.get(**{'month': data.get('month', 0)})
                seasonality_value_instance.percentage = data.get('percentage')
                seasonality_value_instance.save()
            except Exception as ex:
                form = SeasonalityValuesForm()
                return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Seasonality Value', 'message': 'Seasonality Value Successfully Updated'})
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'action': 'edit'})