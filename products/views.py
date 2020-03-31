from django.shortcuts import render
from .forms import ProductForm, CostOfSaleForm, ExpenseForm, ProductSeasonalityRampUpAssignment, TaxForm, AddNProductForm
from .forms import ProductEditForm, ExpenseEditForm, CostOfSaleEditForm, TaxEditForm, ProductAssignmentEditForm
from .models import Product, CostOfSale, Expense, Tax, ProductSeasonalityRampUp
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
    return render(request, 'products/product.html', {'form': form, 'action': 'add'})


def add_n_product(request):
    if request.method == 'POST':
        form = AddNProductForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product_count = range(int(data['product_count']))
                form = ProductForm()
            except Exception as ex:
                form = ProductForm()
                return render(request, 'products/product.html', {'form': form, 'errors': ex})
            return render(request, 'products/product.html', {'form': form, 'product_count': product_count})
    else:
        form = AddNProductForm()
    return render(request, 'products/add_n_products.html', {'form': form, 'action': 'add'})


def edit_product(request):
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product_instance = Product.objects.get(id=data.get('name'))
                form = ProductForm({
                    'name': product_instance.name,
                    'average_unit_price': product_instance.average_unit_price,
                    'average_quantity_per_month': product_instance.average_quantity_per_month,
                    'projection_start': product_instance.projection_start
                })
            except Exception as ex:
                form = ProductEditForm({'name': data.get('name')})
                return render(request, 'products/product.html', {'form': form, 'action': 'edit', 'errors': ex})
            return render(request, 'products/product.html', {'form': form, 'action': 'update'})
    else:
        form = ProductEditForm()
    return render(request, 'products/product.html', {'form': form, 'action': 'edit'})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                expense_instance = Expense(**form.cleaned_data)
                expense_instance.save()
            except Exception as ex:
                form = ExpenseForm()
                return render(request, 'products/expense.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Expense', 'message': 'Expense Successfully Added'})
    else:
        form = ExpenseForm()
    return render(request, 'products/expense.html', {'form': form, 'action': 'add'})


def edit_expense(request):
    if request.method == 'POST':
        form = ExpenseEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                expense_instance = Expense.objects.get(id=data.get('description'))
                form = ExpenseForm({
                    'description': expense_instance.description,
                    'is_fixed': expense_instance.is_fixed,
                    'value': expense_instance.value
                })
            except Exception as ex:
                form = ExpenseEditForm()
                return render(request, 'products/expense.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'products/expense.html', {'form': form, 'action': 'update'})
    else:
        form = ExpenseEditForm()
    return render(request, 'products/expense.html', {'form': form, 'action': 'edit'})


def update_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                expense_instance = Expense.objects.get(description__iexact=data.get('description'))
                expense_instance.is_fixed = data.get('is_fixed')
                expense_instance.value = data.get('value')
                expense_instance.save()
            except Exception as ex:
                form = ExpenseForm()
                return render(request, 'products/expense.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Expense', 'message': 'Expense Successfully Updated'})
    else:
        form = ExpenseForm()
    return render(request, 'products/expense.html', {'form': form, 'action': 'add'})


def update_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product_instance = Product.objects.get(name__iexact=data.get('name'))
                product_instance.average_unit_price = data.get('average_unit_price')
                product_instance.projection_start = data.get('projection_start')
                product_instance.average_quantity_per_month = data.get('average_quantity_per_month')
                product_instance.save()
            except Exception as ex:
                form = ProductForm()
                return render(request, 'products/product.html', {'form': form, 'action': 'update', 'errors': ex})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Product', 'message': 'Product Successfully Updates'})
    else:
        form = ProductForm()
    return render(request, 'products/product.html', {'form': form, 'action': 'add'})


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
                return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Cost Of Sale', 'message': 'Cost Of Sale Successfully Added'})
    else:
        form = CostOfSaleForm()
    return render(request, 'products/cost_of_sale.html', {'form': form, 'action': 'add'})


def edit_cost_of_sale(request):
    if request.method == 'POST':
        form = CostOfSaleEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                cost_of_sale_instance = CostOfSale.objects.get(product_id=data['product'])
                form = CostOfSaleForm({
                    'product': cost_of_sale_instance.product.id,
                    'percentage': cost_of_sale_instance.percentage
                })
            except Exception as ex:
                form = CostOfSaleEditForm()
                return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'products/cost_of_sale.html', {'form': form, 'action': 'update'})
    else:
        form = CostOfSaleEditForm()
    return render(request, 'products/cost_of_sale.html', {'form': form, 'action': 'edit'})


def update_cost_of_sale(request):
    if request.method == 'POST':
        form = CostOfSaleForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                cost_of_sale_instance = CostOfSale.objects.get(product_id=data['product'])
                cost_of_sale_instance.percentage = data.get('percentage')
                cost_of_sale_instance.save()
            except Exception as ex:
                form = CostOfSaleForm()
                return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Cost Of Sale', 'message': 'Cost Of Sale Successfully Updated'})
    else:
        form = CostOfSaleForm()
    return render(request, 'products/cost_of_sale.html', {'form': form, 'action': 'add'})


def add_product_assignment(request):
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
                return render(
                    request,
                    'products/product_assign_seasonality_rampup.html', {'form': form, 'errors': ex , 'action' : 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Product Assignment', 'message': 'Product Assignment Successfully Added'})
    else:
        form = ProductSeasonalityRampUpAssignment()
    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'action': 'add'})


def edit_product_assignment(request):
    if request.method == 'POST':
        form = ProductAssignmentEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product_instance = ProductSeasonalityRampUp.objects.get(product_id=data['product'])
                form = ProductSeasonalityRampUpAssignment({
                    'product': product_instance.product.id,
                    'seasonality': product_instance.seasonality.id,
                    'rampup': product_instance.rampup.id
                })
            except Exception as ex:
                form = ProductAssignmentEditForm()
                return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'action': 'edit'})
            return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'action': 'update'})
    else:
        form = ProductAssignmentEditForm()
    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'action': 'edit'})


def update_product_assignment(request):
    if request.method == 'POST':
        form = ProductSeasonalityRampUpAssignment(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                product_instance = ProductSeasonalityRampUp.objects.get(product_id=data['product'])
                product_instance.seasonality.id = data.get('seasonality')
                product_instance.rampup.id = data.get('rampup')
                product_instance.save()
            except Exception as ex:
                form = ProductSeasonalityRampUpAssignment()
                return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Product Assignment', 'message': 'Product Assignment Successfully Updated'})
    else:
        form = ProductSeasonalityRampUpAssignment()
    return render(request, 'products/product_assign_seasonality_rampup.html', {'form': form, 'action': 'add'})


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
                    return render(request, 'products/tax.html', {'form': form, 'errors': '', 'action': 'add'})
                tax = Tax(**data)
                tax.save()
            except Exception as ex:
                form = TaxForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex, 'action': 'add'})
            return render(request, 'dates/success.html', {'btn_name': 'Add Another Tax Value', 'message': 'Tax Successfully Added'})
    else:
        form = TaxForm()
    return render(request, 'products/tax.html', {'form': form, 'action': 'add'})


def edit_tax_value(request):
    if request.method == 'POST':
        form = TaxEditForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                tax_instance = Tax.objects.get(financial_year_id=data.get('financial_year'))
                form = TaxForm({
                    'financial_year': tax_instance.financial_year.id,
                    'tax_percentage': tax_instance.tax_percentage
                })
            except Exception as ex:
                form = TaxEditForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex, 'action': 'edit'})
            return render(request, 'products/tax.html', {'form': form, 'action': 'update'})
    else:
        form = TaxEditForm()
    return render(request, 'products/tax.html', {'form': form, 'action': 'edit'})


def update_tax_value(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                tax_instance = Tax.objects.get(financial_year_id=int(data.get('financial_year')))
                tax_instance.tax_percentage = data.get('tax_percentage')
                tax_instance.save()
            except Exception as ex:
                form = TaxForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(request, 'dates/success.html', {'btn_name': 'Update Another Tax Value', 'message': 'Tax Successfully Updated'})
    else:
        form = TaxForm()
    return render(request, 'products/tax.html', {'form': form, 'action': 'add'})