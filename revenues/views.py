from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from revenues.models import Revenue
from revenues.forms import GenerateRevenuePrediction
from products.models import Product, ProductSeasonalityRampUp, CostOfSale
from reportlab.pdfgen import canvas


class RevenueInput(CreateView):
    model = Revenue
    template_name = 'revenues/revenue.html'
    
    fields = '__all__'


def generate_revenue_projection(request):
    if request.method == 'POST':
        form = GenerateRevenuePrediction(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data.get('product')
            try:
                if int(form_data['product']) != 0:
                    product_instance = Product.objects.get(id=form_data['product'])
                else:
                    product_instance = Product.objects.all()
                assignment_instance = ProductSeasonalityRampUp.objects.filter(product_id__in=product_instance.values_list('id') if int(form_data['product']) == 0 else [form_data['product']])
                cost_of_sale_instance = CostOfSale.objects.filter(product_id__in=product_instance.values_list('id') if int(form_data['product']) == 0 else [form_data['product']])
                if product_instance and assignment_instance and cost_of_sale_instance:
                    # check if seasonality and ream up is not empty.
                    if assignment_instance.seasonality is None:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    if assignment_instance.rampup is None:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    # check if seasonality and ramp up values are assigned.
                    if len(assignment_instance.seasonality.seasonality_values.all()) == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    if len(assignment_instance.rampup.rampup_values.all()) == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                # all checks succeeded, perform revenue predictions.
                # require: product, financial year & month
                # check financial year
                if not form_data.get('financial_year'):
                    pass
                if not form_data.get('month'):
                    pass
                
                form = GenerateRevenuePrediction(request.POST)
                return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
            except (KeyError, Product.DoesNotExist, ProductSeasonalityRampUp.DoesNotExist, CostOfSale.DoesNotExist) as ex:
                form = GenerateRevenuePrediction(request.POST)
                return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
    else:
        form = GenerateRevenuePrediction()
    return render(request, 'revenues/revenue.html', {'form': form, 'action': 'generate'})
