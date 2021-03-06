from django.http import QueryDict
from django.shortcuts import render

from dates.views import already_created_dates
from .forms import ProductForm, CostOfSaleForm, ExpenseForm, ProductSeasonalityRampUpAssignment, TaxForm, \
    AddNProductForm, AddNExpenseForm, AddNTaxForm
from .forms import ProductEditForm, ExpenseEditForm, CostOfSaleEditForm, TaxEditForm, ProductAssignmentEditForm
from .models import Product, CostOfSale, Expense, Tax, TaxValue
from seasonality.models import Seasonality
from rampup.models import RampUp
from dates.models import FinancialYear


def create_product(request):
    if request.method == 'POST':
        query_data = dict(request.POST)
        data = {
            'name': query_data.get('name'),
            'projection_start': query_data.get('projection_start'),
            'average_unit_price': query_data.get('average_unit_price'),
            'average_quantity_per_month': query_data.get('average_quantity_per_month'),
        }
        errors = list()
        for index, name in enumerate(data.get('name')):
            form_data = {
                'name': name,
                'projection_start': data.get('projection_start')[index],
                'average_unit_price': data.get('average_unit_price')[index],
                'average_quantity_per_month': data.get('average_quantity_per_month')[index],
                
            }
            query = QueryDict('', mutable=True)
            query.update(form_data)
            form = ProductForm(query)
            if form.is_valid():
                try:
                    form_data = form.cleaned_data
                    new_product_instance = Product(**form_data)
                    new_product_instance.save()
                except Exception as ex:
                    errors.append(ex)
        if errors:
            form = ProductForm()
            return render(request, 'products/product.html', {'form': form, 'errors': errors, 'action': 'add'})
        return render(request, 'dates/success.html', {'btn_name': 'Add Another Product', 'message': 'Product Successfully Added', 'view': 'product'})
    else:
        form = ProductForm()
        return render(request, 'products/product.html', {'form': form, 'action': 'add'})


def view_product(request):
    product = Product.objects.all().order_by('-id')
    return render(request, 'products/view_product.html', context={'data': enumerate(product)})


def view_expense(request):
    expenses = Expense.objects.all().order_by('-id')
    return render(request, 'products/view_expense.html', context={'data': enumerate(expenses)})


def add_n_product(request):

    is_loaded = already_created_dates('product', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Updates',
            'view': 'product',
            'action': 'review',
            'message': 'Product Options'
        })
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
            return render(request, 'products/product.html', {'form': form, 'product_count': product_count, 'action': 'add'})
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


def add_n_expense(request):
    if request.method == 'POST':
        form = AddNExpenseForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                expense_count = range(int(data['expense_count']))
                form = ExpenseForm()
            except Exception as ex:
                form = AddNExpenseForm()
                return render(request, 'products/add_n_expenses.html', {'form': form, 'errors': ex})
            return render(request, 'products/expense.html',
                          {'form': form, 'expense_count': expense_count, 'action': 'add', 'expense_type': data['expense_type']})
    else:
        form = AddNExpenseForm()
    return render(request, 'products/add_n_expenses.html', {'form': form, 'action': 'add'})


def add_expense(request):
    if request.method == 'POST':
        query_dict = dict(request.POST)
        data = {
            'description': query_dict.get('description'),
            'expense_type': query_dict.get('expense_type'),
            'is_fixed': query_dict.get('is_fixed'),
            'value': query_dict.get('value')
        }
        errors = list()
        for index, description in enumerate(data.get('description')):
            form_data = {
                'description': description,
                'is_fixed': data.get('is_fixed')[index],
                'expense_type': int(data.get('expense_type')[0]),
                'value': data.get('value')[index]
            }
            query = QueryDict('', mutable=True)
            query.update(form_data)
            form = ExpenseForm(form_data)
            if form.is_valid():
                try:
                    expense_instance = Expense(**form.cleaned_data)
                    expense_instance.save()
                except Exception as ex:
                    errors.append(ex)
        if errors:
            form = ExpenseForm()
            return render(request, 'products/expense.html', {'form': form, 'errors': errors, 'action': 'add'})
        return render(request, 'dates/success.html', {'btn_name': 'Add Another Expense', 'message': 'Expense(s) Successfully Added', 'view': 'expense'})
    else:
        form = ExpenseForm()
        return render(request, 'products/expense.html', {'form': form, 'action': 'add'})


def expense_type(exp_type):
    return exp_type not in [-1, 0]


def edit_expense(request):
    if request.method == 'POST':
        request_data = dict(request.POST)
        errors = list()
        for index, expense in enumerate(request_data.get('description')):
            expense_data = {
                'description': expense,
                'expense_type': int(request_data.get('expense_type')[index]),
                'is_fixed': request_data.get('is_fixed')[index],
                'value': request_data.get('value')[index],
            }
            form = ExpenseForm(expense_data)
            if form.is_valid():
                try:
                    data = form.cleaned_data
                    expense_instance = Expense.objects.get(description=data.get('description'))
                    if expense_instance.value != data['value'] or expense_instance.expense_type != data['expense_type']:
                        expense_instance.value = data['value']
                        expense_instance.expense_type = data['expense_type']
                        expense_instance.save()
                    if expense_instance.is_fixed != expense_type(int(data['is_fixed'])):
                        expense_instance.is_fixed = expense_type(int(data['is_fixed']))
                        expense_instance.save()
                except Exception as ex:
                    errors.append(ex)
        if len(errors) > 0:
            form = ExpenseEditForm()
            expenses = Expense.objects.values_list('id', 'description', 'is_fixed', 'value')
            return render(request, 'products/expense.html', {'form': form, 'errors': errors, 'action': 'edit', 'expenses': expenses})
        return render(
            request,
            'dates/success.html',
            {
                'btn_name': 'Update',
                'message': 'Successfully Updated',
                'view': 'expense',
                'action': 'review'
            }
        )
    else:
        form = ExpenseEditForm()
        expenses = Expense.objects.values_list('id', 'description', 'is_fixed', 'value', 'expense_type')
        
        return render(request, 'products/expense.html', {'form': form, 'action': 'edit', 'expenses': expenses, 'expense_types': Expense.EXPENSE_TYPE})


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
            return render(
                request,
                'dates/success.html',
                {'btn_name': 'Update', 'message': 'Product Options', 'view': 'product', 'action': 'review'}
            )
    else:
        form = ProductForm()
    return render(request, 'products/product.html', {'form': form, 'action': 'add'})


def create_cost_of_sale(request):
    is_loaded = already_created_dates('cost_of_sale', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Updates',
            'view': 'cost_of_sale',
            'action': 'review',
            'message': 'Cost Of Sale Options'
        })
    if request.method == 'POST':
        request_data = dict(request.POST)
        errors = list()
        for index, product in enumerate(request_data.get('product')):
            product_percentage = request_data.get('percentage')[index]
            product_data = {
                'product': product,
                'percentage': product_percentage
            }
            form = CostOfSaleForm(product_data)
            if form.is_valid():
                try:
                    data = form.cleaned_data
                    cost_of_sale_instance = CostOfSale.objects.filter(product__name=data.get('product'))
                    if cost_of_sale_instance.count() == 0:
                        product = Product.objects.get(name=data.get('product'))
                        data['product'] = product
                        data['percentage'] = int(data['percentage'])
                        cost_of_sale_instance = CostOfSale(**data)
                        cost_of_sale_instance.save()
                    else:
                        percent = cost_of_sale_instance.first()
                        percent.percentage = data.get('percentage')
                        percent.save()
                except Exception as ex:
                    errors.append(ex)
        if len(errors) > 0:
            form = CostOfSaleForm()
            return render(request, 'products/cost_of_sale.html', {'form': form, 'errors': errors, 'action': 'add'})
        return render(
            request,
            'dates/success.html',
            {
                'btn_name': 'Update',
                'action': 'add',
                'view': 'cost_of_sale',
                'message': 'Cost Of Sale Successfully Added'
            }
        )
    else:
        form = CostOfSaleForm()
        products = Product.objects.values_list('id', 'name', 'product_cost_of_sale__percentage')
        products_without_cost_of_sale = list(filter(lambda product_cost_of_sale: product_cost_of_sale[2] is None, products))
        return render(
            request,
            'products/cost_of_sale.html',
            {
                'form': form,
                'action': 'add',
                'products': products_without_cost_of_sale
            }
        )


def edit_cost_of_sale(request):
    if request.method == 'POST':
        request_data = dict(request.POST)
        errors = list()
        for index, product in enumerate(request_data.get('product')):
            data = {
                'product': product,
                'percentage': request_data.get('percentage')[index],
            }
            form = CostOfSaleForm(data)
            if form.is_valid():
                try:
                    form_data = form.cleaned_data
                    cost_of_sale_instance = CostOfSale.objects.get(product__name=form_data['product'])
                    if cost_of_sale_instance.percentage == float(form_data['percentage']):
                        continue
                    cost_of_sale_instance.percentage = float(form_data['percentage'])
                    cost_of_sale_instance.save()
                except Exception as ex:
                    errors.append(ex)
        if len(errors) > 0:
            form = CostOfSaleEditForm()
            products = Product.objects.values_list('id', 'name', 'product_cost_of_sale__percentage')
            products = [list(product) for product in products]
            for product in products:
                if product[2]:
                    product[2] = product[2] * 100
            return render(
                request,
                'products/cost_of_sale.html',
                {
                    'form': form,
                    'errors': errors,
                    'action': 'edit',
                    'products': products
                })
        return render(
            request,
            'dates/success.html',
            {
                'btn_name': 'Update',
                'action': 'review',
                'view': 'cost_of_sale',
                'message': 'Successfully Updated'
            }
        )
    else:
        form = CostOfSaleEditForm()
        products = Product.objects.values_list('id', 'name', 'product_cost_of_sale__percentage')
        products = [list(product) for product in products]
        for product in products:
            if product[2]:
                product[2] = product[2] * 100
        return render(request, 'products/cost_of_sale.html', {'form': form, 'action': 'edit', 'products': products})


def view_cost_of_sale(request):

    form = CostOfSaleForm()
    products = list(Product.objects.values_list('id', 'name', 'product_cost_of_sale__percentage'))
    products = [list(product) for product in products]
    for product in products:
        if product[2]:
            product[2] = product[2] * 100
    return render(
        request,
        'products/cost_of_sale.html',
        {
            'form': form,
            'action': 'view',
            'view': 'cost_of_sale',
            'products': products
        }
    )


def add_n_tax_values(request):
    if request.method == 'POST':
        form = AddNTaxForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                tax_count = range(int(data['tax_add_count']))
                form = TaxForm()
            except Exception as ex:
                form = AddNTaxForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex, 'action': 'n_add'})
            return render(request, 'products/tax.html',
                          {'form': form, 'tax_count': list(tax_count), 'action': 'add'})
    else:
        form = AddNTaxForm()
    return render(request, 'products/tax.html', {'form': form, 'action': 'n_add'})


def add_tax_value(request):
    is_loaded = already_created_dates('tax', request.GET.get('update'))
    if is_loaded is True:
        return render(request, 'dates/success.html', {
            'btn_name': 'Updates',
            'view': 'tax',
            'action': 'review',
            'message': 'Tax Options'
        })
    if request.method == 'POST':
        query_dict = dict(request.POST)
        data = {
            'financial_year': query_dict.get('financial_year'),
            'tax_percentage': query_dict.get('tax_percentage')
        }
        errors = list()
        for index, financial_year in enumerate(data.get('financial_year')):
            form_data = {
                'financial_year': financial_year,
                'tax_percentage': data.get('tax_percentage')[index]
            }
            query = QueryDict('', mutable=True)
            query.update(form_data)
            form = TaxForm(query)
            if form.is_valid():
                try:
                    form_data = form.cleaned_data
                    financial_year = FinancialYear.objects.filter(description=form_data['financial_year'])
                    if financial_year.count() > 0:
                        form_data['financial_year'] = financial_year.first()
                        form_data['value'] = form_data['tax_percentage']
                        form_data.pop('tax_percentage')
                        tax = TaxValue(**form_data)
                        tax.save()
                except Exception as ex:
                    errors.append(ex)
        if len(errors) > 0:
            form = TaxForm()
            taxes_already_allocated = TaxValue.objects.values_list('financial_year', flat=True)
            unallocated_financial_years = FinancialYear.objects.exclude(
                id__in=taxes_already_allocated
            ).values_list(
                'description', flat=True
            )
            return render(
                request,
                'products/tax.html',
                {
                    'form': form,
                    'errors': errors,
                    'action': 'add',
                    'unallocated_financial_years': unallocated_financial_years
                }
            )
        return render(
            request,
            'dates/success.html',
            {
                'btn_name': 'Add Another Tax Value', 'message':
                'Tax Successfully Added',
                'action': 'add',
                'view': 'tax'
            }
        )
    form = TaxForm()
    taxes_already_allocated = TaxValue.objects.values_list('financial_year', flat=True)
    unallocated_financial_years = FinancialYear.objects.exclude(
        id__in=taxes_already_allocated
    ).values_list(
        'description', flat=True
    )
    return render(
        request,
        'products/tax.html',
        {
            'form': form,
            'action': 'add',
            'unallocated_financial_years': unallocated_financial_years
        }
    )


def edit_tax_value(request):
    if request.method == 'POST':
        query_dict = dict(request.POST)
        data = {
            'financial_year': query_dict.get('financial_year'),
            'tax_percentage': query_dict.get('tax_percentage')
        }
        errors = list()
        for index, financial_year in enumerate(data.get('financial_year')):
            form_data = {
                'financial_year': financial_year,
                'tax_percentage': data.get('tax_percentage')[index]
            }
            query = QueryDict('', mutable=True)
            query.update(form_data)
            form = TaxForm(query)
            if form.is_valid():
                try:
                    form_data = form.cleaned_data
                    tax_instance = TaxValue.objects.get(financial_year__description=form_data.get('financial_year'))
                    if tax_instance.value != float(form_data['tax_percentage']):
                        tax_instance.value = float(form_data['tax_percentage'])
                        tax_instance.save()
                except Exception as ex:
                    errors.append(ex)
        if len(errors) > 0:
            form = TaxForm()
            allocated_financial_years = TaxValue.objects.values_list('financial_year__description', 'value')
            return render(
                request,
                'products/tax.html',
                {
                    'form': form,
                    'errors': errors,
                    'action': 'edit',
                    'allocated_financial_years': allocated_financial_years
                }
            )
        return render(
            request,
            'dates/success.html',
            {
                'form': form,
                'action': 'review',
                'view': 'tax',
                'btn_name': 'Update',
                'message': 'Successfully Added Tax Values'
            })
    else:
        form = TaxForm()
        allocated_financial_years = TaxValue.objects.values_list('financial_year__description', 'value')
    return render(
        request,
        'products/tax.html',
        {
            'form': form,
            'action': 'edit',
            'allocated_financial_years': allocated_financial_years
        }
    )


def update_tax_value(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                tax_instance = TaxValue.objects.get(financial_year_id=int(data.get('financial_year')))
                tax_instance.value = data.get('tax_percentage')
                tax_instance.save()
            except Exception as ex:
                form = TaxForm()
                return render(request, 'products/tax.html', {'form': form, 'errors': ex, 'action': 'update'})
            return render(
                request,
                'dates/success.html',
                {
                    'btn_name': 'Update Another Tax Value',
                    'message': 'Tax Successfully Updated',
                    'action': 'review',
                    'view': 'tax'
                }
            )
    else:
        form = TaxForm()
    return render(request, 'products/tax.html', {'form': form, 'action': 'add'})


def view_tax_value(request):
    form = TaxForm()
    taxes = TaxValue.objects.values_list('financial_year__description', 'value')
    return render(request, 'products/tax.html', {'form': form, 'allocated_financial_years': taxes, 'action': 'view', 'view': 'tax'})
