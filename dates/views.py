from django.views.generic.edit import CreateView
from .models import FinancialYear
from django.shortcuts import render, redirect
from .forms import DatesForm


class CreateDates(CreateView):
    model = FinancialYear
    template_name = 'dates/dates_form.html'
    fields = '__all__'


def create_financial_year(request):

    if request.method == 'POST':
        form = DatesForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = DatesForm()
    return render(request, 'dates_form.html', {'form': form})
