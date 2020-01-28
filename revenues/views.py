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
                product_instance = Product.objects.filter(id=form_data['product'])
                assignment_instance = ProductSeasonalityRampUp.objects.filter(product_id=form_data['product'])
                cost_of_sale_instance = CostOfSale.objects.filter(product_id=form_data['product'])
            except (KeyError,) as ex:
                pass
        else:
            pass
    else:
        form = GenerateRevenuePrediction()
    return render(request, 'revenues/revenue.html', {'form': form, 'action': 'generate'})
