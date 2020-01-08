from django.shortcuts import render
from .forms import SeasonalityForm, SeasonalityValuesForm
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
                    return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ''})
                seasonality_instance = Seasonality(**data)
                seasonality_instance.save()
                if len(vals) > 0:
                    seasonality_instance.seasonality_values.add(*vals)
                    seasonality_instance.save()
            except Exception as ex:
                form = SeasonalityForm()
                return render(request, 'seasonality/product_seasonality.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Seasonality', 'message': 'Seasonality Successfully Added'})
    else:
        form = SeasonalityForm()
    return render(request, 'seasonality/product_seasonality.html', {'form': form})


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
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Seasonality Value', 'message': 'Seasonality Value Successfully Added'})
    else:
        form = SeasonalityValuesForm()
    return render(request, 'seasonality/product_seasonality_values.html', {'form': form})