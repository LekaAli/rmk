from django.shortcuts import render
from .forms import ProductForm, CostOfSaleForm, ExpenseForm, ProductSeasonalityRampUpAssignment, TaxForm
from .models import Product, CostOfSale, Expense, ProductSeasonalityRampUp, Tax
from seasonality.models import Seasonality
from rampup.models import RampUp
from dates.models import FinancialYear


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                new_product_instance = Product(**data)
                new_product_instance.save()
            except Exception as ex:
                form = ProductForm()
                return render(request, 'products/product.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Product', 'message': 'Product Successfully Added'})
    else:
        form = ProductForm()
    return render(request, 'products/product.html', {'form': form})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                expense_instance = Expense(**form.cleaned_data)
                expense_instance.save()
            except Exception as ex:
                form = ExpenseForm()
                return render(request, 'products/expense.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Expense', 'message': 'Expense Successfully Added'})
    else:
        form = ExpenseForm()
    return render(request, 'products/expense.html', {'form': form})


def create_cost_of_sale(request):
    if request.method == 'POST':
        form = CostOfSaleForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product = Product.objects.filter(id=data['product'])
                if product.count() > 0:
                    data['product'] = product[0]
                else:
                    form = CostOfSaleForm()
                    return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': ''})
                cost_of_sale_instance = CostOfSale(**data)
                cost_of_sale_instance.save()
            except Exception as ex:
                form = CostOfSaleForm()
                return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Cost Of Sale', 'message': 'Cost Of Sale Successfully Added'})
    else:
        form = CostOfSaleForm()
    return render(request, 'products/cost_of_sale.html', {'form': form})


def product_seasonality_rampup_assignment(request):
    if request.method == 'POST':
        form = ProductSeasonalityRampUpAssignment(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product = Product.objects.filter(id=data['product'])
                if product.count() > 0:
                    data['product'] = product[0]
                else:
                    form = ProductSeasonalityRampUpAssignment()
                    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'errors': ''})
                seasonality = Seasonality.objects.filter(id=data['seasonality'])
                rampup = RampUp.objects.filter(id=data['rampup'])
                if seasonality.count() > 0 and rampup.count() > 0:
                    data['seasonality'] = seasonality[0]
                    data['rampup'] = rampup[0]
                else:
                    form = ProductSeasonalityRampUpAssignment()
                    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'errors': ''})
                product_seasonality_rampup_assignment = ProductSeasonalityRampUp(**data)
                product_seasonality_rampup_assignment.save()
            except Exception as ex:
                form = ProductSeasonalityRampUpAssignment()
                return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Product Assignment', 'message': 'Product Assignment Successfully Added'})
    else:
        form = ProductSeasonalityRampUpAssignment()
    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form})


def add_tax_value(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                financial_year = FinancialYear.objects.filter(id=data['financial_year'])
                if financial_year.count() > 0:
                    data['financial_year'] = financial_year[0]
                else:
                    form = TaxForm()
                    return render(request, 'products/tax.html', {'form': form, 'errors': ''})
                tax = Tax(**data)
                tax.save()
            except Exception as ex:
                form = TaxForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Tax Value', 'message': 'Tax Successfully Added'})
    else:
        form = TaxForm()
    return render(request, 'products/tax.html', {'form': form})



