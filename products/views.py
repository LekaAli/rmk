from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductForm, CostOfSaleForm


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = ProductForm()
    return render(request, 'products/product.html', {'form': form})

def create_cost_of_sale(request):
    if request.method == 'POST':
        form = CostOfSaleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('/'))
    else:
        form = CostOfSaleForm()
    return render(request, 'products/product.html', {'form': form})



