from django.db import IntegrityError
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


def create_linked_financial_years(f_year_instance, year_count=5):
    
    if year_count not in ['', '1']:
        year_count = int(year_count)
        year_start_date = f_year_instance.end_date
        for year_count in range(2, year_count + 1):
            if isinstance(year_start_date, str):
                from datetime import date, timedelta
                date_chunks = [int(d_part) for d_part in year_start_date.split('-')]
                year_start_date = date(*date_chunks)
            start_date = year_start_date + timedelta(days=1)
            desc = ''.join(['Year ', '%s' % year_count])
            fin_year = FinancialYear.objects.filter(description=desc)
            if fin_year:
                FinancialYear.objects.exclude(description='Year 1').delete()
            f_year = FinancialYear(**{'description': desc, 'start_date': start_date})
            f_year.save()
            year_start_date = f_year.end_date


def create_dates(request):
    
    if request.method == 'POST':
        form_data = dict(request.POST)
        errors = list()
        try:
            f_year_instance = FinancialYear(**{
                'start_date': form_data['start_date'][0],
                'end_date': form_data['end_date'][0],
                'description': 'Year 1'
            })
            f_year_instance.save()
        except IntegrityError as ex:
            f_year = FinancialYear.objects.filter(description='Year 1')
            f_y_instance = f_year.first()
            f_y_instance.start_date = form_data['start_date'][0]
            f_y_instance.end_date = form_data['end_date'][0]
            f_y_instance.save()
        except Exception as ex:
            errors.append(ex)
        if errors:
            form = forms.DatesForm()
            return render(request, 'dates/dates_form.html', {'form': form, 'errors': errors})
        create_linked_financial_years(f_year_instance, form_data['year_count'][0])
        return render(request, 'dates/success.html', {'btn_name': 'Add Another Financial Year', 'message': 'Successfully Added Financial Year'})
    else:
        form = forms.DatesForm()
    return render(request, 'dates/dates_form.html', {'form': form})


def manage_inflation_values(request):
    is_loaded = already_created_dates('inflation', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Update',
            'view': 'inflation',
            'action': 'review',
            'message': 'Inflation Options'
        })
    financial_years_count = FinancialYear.objects.values_list('description', flat=True)
    if request.method == 'POST':
        errors = list()
        form = forms.DatesForm(request.POST)
        data = dict(form.data)
        inflation_values = data.get('inflation')
        for index in range(1, len(inflation_values) + 1):
            f_year = FinancialYear.objects.filter(description='Year %s' % index)
            if f_year:
                f_year_instance = f_year.first()
                f_year_instance.inflation = float(inflation_values[index-1])
                f_year_instance.save()
            else:
                errors.append('Year %s not found' % index)
        if errors:
            pass
        return render(request, 'dates/success.html',
                      {'btn_name': 'Updates', 'view': 'inflation', 'action': 'review', 'message': 'Inflation Options'})
    else:
        form = forms.DatesForm()
    return render(request, 'dates/manage_inflation.html', {'form': form, 'years': financial_years_count})


def edit_inflation(request):
    years = FinancialYear.objects.all().order_by('id').values_list('id', 'description')
    if request.method == 'POST':
        errors = list()
        try:
            form = forms.EditDates(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                year = FinancialYear.objects.get(id=data['description'])
                year_data = {
                    'description': year.description,
                    'start_date': year.start_date,
                    'end_date': year.end_date,
                    'inflation': year.inflation,
                }
                form = forms.DatesForm(year_data)
                return render(request, 'dates/manage_inflation.html', {'form': form, 'view': 'inflation', 'action': 'update', 'years': years, 'selected': year.id})
        except Exception as ex:
            errors.append(ex)
        if len(errors) > 0:
            form = forms.EditDates()
            return render(request, 'dates/manage_inflation.html', {'form': form, 'view': 'inflation', 'action': 'edit'})
    form = forms.EditDates()
    return render(
        request,
        'dates/manage_inflation.html',
        {'form': form, 'view': 'inflation', 'action': 'edit', 'years': years}
    )
    
    
def update_inflation(request):
    years = FinancialYear.objects.all().order_by('id').values_list('id', 'description')
    if request.method == 'POST':
        form = forms.InflationUpdateForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                financial_year_instance = FinancialYear.objects.get(id=data['description'])
                financial_year_instance.inflation = data['inflation']
                financial_year_instance.save()
                return render(
                    request,
                    'dates/success.html',
                    {
                        'btn_name': 'Update',
                        'message': 'Financial Year Options',
                        'view': 'inflation',
                        'action': 'review',
                    }
                )
            except Exception as ex:
                form = forms.DatesForm()
                return render(request, 'dates/manage_inflation.html', {'form': form, 'view': 'inflation', 'action': 'update', 'years': years})
    form = forms.DatesForm()
    return render(request, 'dates/manage_inflation.html', {'form': form, 'view': 'inflation', 'action': 'update', 'years': years})


def advanced_create_dates(request):
    
    is_loaded = already_created_dates('dates', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Update',
            'view': 'dates',
            'action': 'review',
            'message': 'Financial Year Options'
        })
    if request.method == 'POST':
        # process POST request data before check them against the form
        form = forms.AdvancedDatesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            year_count = data.get('year_counts', 0)
            form = forms.DatesForm()
            return render(request, 'dates/dates_form.html', {'year_count': year_count, 'form': form, 'action': 'add'})
    else:
        form = forms.AdvancedDatesForm()
    return render(request, 'dates/add_n_financial_years.html', {'form': form, 'action': 'add'})


def view_dates(request):
    years = FinancialYear.objects.all().order_by('id')
    return render(request, 'dates/view_dates.html', context={'data': enumerate(years), 'view': 'dates'})


def view_inflation(request):
    years = FinancialYear.objects.all().order_by('id')
    return render(request, 'dates/view_dates.html', context={'data': enumerate(years), 'view': 'inflation'})


def edit_dates(request):
    year = FinancialYear.objects.all().order_by('id').values_list('id', 'description')
    if request.method == 'POST':
        form = forms.EditDates(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                financial_year_instance = FinancialYear.objects.get(id=data['description'])
                form = forms.DatesForm({
                    'description': financial_year_instance.description,
                    'start_date': financial_year_instance.start_date,
                    'end_date': financial_year_instance.end_date,
                    'inflation': financial_year_instance.inflation
                    })
                return render(
                    request,
                    'dates/dates_form.html',
                    {'form': form, 'action': 'update', 'years': year, 'selected': financial_year_instance.id}
                )
            except Exception as ex:
                form = forms.EditDates()
                return render(request, 'dates/dates_form.html', {'form': form, 'errors': ex})
    form = forms.EditDates()
    return render(request, 'dates/dates_form.html', {'action': 'edit', 'form': form, 'years': year})


def update_dates(request):
    if request.method == 'POST':
        form = forms.UpdateForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                financial_year_instance = FinancialYear.objects.get(id=data['description'])
                financial_year_instance.start_date = data['start_date']
                financial_year_instance.end_date = data['end_date']
                financial_year_instance.save()
                return render(
                    request,
                    'dates/success.html',
                    {
                        'btn_name': 'Update',
                        'message': 'Financial Year Options',
                        'view': 'dates',
                        'action': 'review',
                    }
                )
            except Exception as ex:
                form = forms.EditDates()
                return render(request, 'dates/dates_form.html', {'form': form, 'errors': ex})
    form = forms.UpdateForm()
    return render(request, 'dates/dates_form.html', {'action': 'add', 'form': form})


def product_count_check(product_id_lst, type_flag='seasonality'):

    from rampup.models import RampUpValue
    from seasonality.models import SeasonalityValue
    if type_flag == 'rampup':
        product_check_results = map(lambda x: RampUpValue.objects.filter(product=x).count() > 1, product_id_lst)
    else:
        product_check_results = map(lambda x: SeasonalityValue.objects.filter(product=x).count() > 0, product_id_lst)
    for product_check_result in product_check_results:
        if product_check_result is False:
            return False
    return True

    
def already_created_dates(view_name, flag):
    from products.models import Product
    products = Product.objects.values_list('id', flat=True)
    view_models_dict = {
        'dates': FinancialYear.objects.all().count() > 0,
        'inflation': FinancialYear.objects.all().count() > 0,
        'rampup': product_count_check(products, 'rampup'),
        'seasonality': product_count_check(products),
        'product': Product.objects.all().count() > 0,
        'cost_of_sale': len([product for product in Product.objects.values_list('product_cost_of_sale__percentage', flat=True) if product is None]) == 0,
    }
    return view_models_dict.get(view_name, False) if flag != 'review' else False

