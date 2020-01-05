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
    year_start_date = f_year_instance.end_date
    for year_count in range(2, year_count + 1):
        desc = ''.join(['Year ', '%s' % year_count])
        f_year = FinancialYear(**{'description': desc, 'start_date': year_start_date})
        f_year.save()
        year_start_date = f_year.end_date


def create_dates(request):
    if request.method == 'POST':
        form = forms.DatesForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                if 'year_counts' in data:
                    year_count = data.pop('year_counts')
                new_f_year = FinancialYear(**data)
                new_f_year.save()
                create_linked_financial_years(new_f_year, year_count)
            except Exception as ex:
                form = forms.DatesForm()
                return render(request, 'dates/dates_form.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'message': 'Successfully Added Financial Year'})
    else:
        form = forms.DatesForm()
    return render(request, 'dates/dates_form.html', {'form': form})

