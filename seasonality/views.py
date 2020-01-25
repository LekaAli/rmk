from django.shortcuts import render
from .forms import SeasonalityForm, SeasonalityValuesForm, SeasonalityValuesEditForm, SeasonalityEditForm
from .models import Seasonality, SeasonalityValue
from dates.models import FinancialYear


def add_seasonality(request):
    if request.method == 'POST':
        form = SeasonalityForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                vals = data.pop('seasonality_values')
                year_instance = FinancialYear.objects.filter(id=data['year'])
                if year_instance.count() > 0:
                    data['year'] = year_instance[0]
                else:
                    form = SeasonalityForm()
                    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': '', 'action': 'add'})
                seasonality_instance = Seasonality(**data)
                seasonality_instance.save()
                if len(vals) > 0:
                    seasonality_instance.seasonality_values.add(*vals)
                    seasonality_instance.save()
            except Exception as ex:
                form = SeasonalityForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Seasonality', 'message': 'Seasonality Successfully Added'})
    else:
        form = SeasonalityForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'add'})


def edit_seasonality(request):
    if request.method == 'POST':
        form = SeasonalityEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_instance = Seasonality.objects.get(id=data.get('name'))
                form = SeasonalityForm({
                    'name': seasonality_instance.name,
                    'seasonality_type': seasonality_instance.seasonality_type,
                    'seasonality_values': list(seasonality_instance.seasonality_values.values_list('id')),
                    'year': seasonality_instance.year.id,
                    'will_roll_over': seasonality_instance.will_roll_over
                })
            except Exception as ex:
                form = SeasonalityEditForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'update'})
    else:
        form = SeasonalityEditForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'edit'})


def update_seasonality(request):
    if request.method == 'POST':
        form = SeasonalityForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_instance = Seasonality.objects.get(name__iexact=data.get('name'))
                seasonality_instance.seasonality_type = data.get('seasonality_type')
                seasonality_instance.seasonality_values.set(data.get('seasonality_values'))
                seasonality_instance.year.id = data.get('year')
                seasonality_instance.will_roll_over = data.get('will_roll_over')
                seasonality_instance.save()
            except Exception as ex:
                form = SeasonalityForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Seasonality', 'message': 'Seasonality Successfully Updated'})
    else:
        form = SeasonalityForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'action': 'add'})


def add_seasonality_value(request):
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


def edit_seasonality_value(request):
    if request.method == 'POST':
        form = SeasonalityValuesEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                seasonality_value_instance = SeasonalityValue.objects.get(**data)
                form = SeasonalityValuesForm({
                    'month': seasonality_value_instance.month,
                    'percentage': seasonality_value_instance.percentage
                })
            except Exception as ex:
                form = SeasonalityValuesEditForm()
                return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'seasonality/product_seasonality_values.html', {'form': form, 'action': 'update'})
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