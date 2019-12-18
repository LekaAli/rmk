from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductForm, CostOfSaleForm, ExpenseForm
from .models import Product, CostOfSale, Expense


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                data['projection_start'] = data['projection_start'].month
                new_product_instance = Product(**data)
                new_product_instance.save()
            except Exception as ex:
                form = ProductForm()
                return render(request, 'products/product.html', {'form': form, 'errors': ex})
            return render(request, 'dates/success.html', {'message': 'Product Successfully Added'})
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
            return render(request, 'dates/success.html', {'message': 'Expense Successfully Added'})
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
            return render(request, 'dates/success.html', {'message': 'Cost Of Sale Successfully Added'})
    else:
        form = CostOfSaleForm()
    return render(request, 'products/cost_of_sale.html', {'form': form})



