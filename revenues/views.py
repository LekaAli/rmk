from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from revenues.models import Revenue
from revenues.forms import GenerateRevenuePrediction
from products.models import Product, ProductSeasonalityRampUp, CostOfSale, GrossProfit, ProfitBeforeTax, Tax, NetProfit
from django.db.models.query import QuerySet
from rmkplatform.constants import MONTHS
from dates.models import FinancialYear
from utils.pdf_creator import html_to_pdf_creator


class RevenueInput(CreateView):
    model = Revenue
    template_name = 'revenues/revenue.html'
    
    fields = '__all__'


def generate_revenue_projection(request):
    if request.method == 'POST':
        form = GenerateRevenuePrediction(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                if int(form_data['product']) != 0:  # projection for a given product
                    product_instance = Product.objects.get(id=form_data['product'])
                else:  # projection for all available products
                    product_id_lst = Product.objects.all().values_list('id', flat=True)
                    # product_id_lst = product_instance.values_list('id', flat=True)
                assignment_instance = ProductSeasonalityRampUp.objects.filter(
                    product_id__in=product_id_lst if int(form_data['product']) == 0 else [form_data['product']]
                )
                cost_of_sale_instance = CostOfSale.objects.filter(
                    product_id__in=product_id_lst if int(form_data['product']) == 0 else [form_data['product']]
                )
                if product_instance and assignment_instance and cost_of_sale_instance:
                    form = GenerateRevenuePrediction()
                    # check if seasonality and ream up is not empty.
                    if isinstance(assignment_instance, ProductSeasonalityRampUp):
                        if assignment_instance.seasonality is None:
                            return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                        if assignment_instance.rampup is None:
                            return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                        
                        # check if seasonality and ramp up values are assigned.
                        if len(assignment_instance.seasonality.seasonality_values.all()) == 0:
                            return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                        if len(assignment_instance.rampup.rampup_values.all()) == 0:
                            return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    if isinstance(assignment_instance, QuerySet):
                        if len(assignment_instance) == 0:
                            return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})

                if isinstance(cost_of_sale_instance, CostOfSale):
                    if product_instance is None:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                elif isinstance(cost_of_sale_instance, QuerySet):
                    if len(cost_of_sale_instance) == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                else:
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    
                # all checks succeeded, perform revenue predictions.
                # require: product, financial year & month
                # check financial year
                if not form_data.get('year'):
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                if not form_data.get('month'):
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                
                if isinstance(product_instance, QuerySet) and int(form_data.get('month')) == 0:
                    for product in product_instance:
                        current_revenues = Revenue.objects.filter(product=product).values_list('month', 'product_revenue')
                        #Ge ngwaga o le 0 goba 24 Revenue, tswelapele ka go dira di culculation tsa di revenue tsa kgwedi
                        if 0 <= current_revenues.count() < 24:
                            for month in MONTHS[2:]:
                                try:
                                    revenue_instance = Revenue(**{
                                        'product': product,
                                        'financial_year_id': int(form_data.get('year')),
                                        'month': month[0]
                                    })
                                    revenue_instance.save()
                                    gross_profit_instance = GrossProfit(**{
                                        'product': product,
                                        'financial_year_id': int(form_data.get('year')),
                                        'month': month[0] if isinstance(month, tuple) else month,
                                        'cost_of_sale_id': cost_of_sale_instance.filter(product=product).first().id
                                    })
                                    gross_profit_instance.save()
                                except Exception as ex:
                                    pass
                        else:  # Calculate Revenue ka ngwaga eseng ka kgwedi le kgwedi.
                            revenue_instance = Revenue(**{
                                'product': product,
                                'financial_year_id': int(form_data.get('year'))
                            })
                            revenue_instance.save()
                            f_year_instance = FinancialYear.objects.get(id=int(form_data.get('year')))
                            gross_profit_instance = GrossProfit(**{
                                'product': product,
                                'financial_year_id': int(form_data.get('year')),
                                'month': f_year_instance.end_date.month,
                                'cost_of_sale_id': cost_of_sale_instance.filter(product=product).first().id
                            })
                            gross_profit_instance.save()
                    for month in MONTHS[2:]:
                        profit_before_tax_instance = ProfitBeforeTax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0] if isinstance(month, tuple) else month
                        })
                        profit_before_tax_instance.save()
                    
                    for month in MONTHS[2:]:
                        tax_instance = Tax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0] if isinstance(month, tuple) else month,
                            'tax_percentage': form_data.get('tax', 1.0)
                        })
                        tax_instance.save()
                    for month in MONTHS[2:]:
                        net_profit_instance = NetProfit(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0] if isinstance(month, tuple) else month
                        })
                        net_profit_instance.save()
                if isinstance(product_instance, QuerySet) and int(form_data.get('month')) != 0:
                    for product in product_instance:
                        try:
                            revenue_instance = Revenue(**{
                                'product': product,
                                'financial_year_id': int(form_data.get('year')),
                                'month': form_data.get('month')
                            })
                            revenue_instance.save()
                            gross_profit_instance = GrossProfit(**{
                                'product': product,
                                'financial_year_id': int(form_data.get('year')),
                                'month': form_data.get('month'),
                                'cost_of_sale_id': cost_of_sale_instance.filter(product=product).first().id
                            })
                            gross_profit_instance.save()
                            
                        except Exception as ex:
                            pass
                    profit_before_tax_instance = ProfitBeforeTax(**{
                        'financial_year_id': int(form_data.get('year')),
                        'month': form_data.get('month')
                    })
                    profit_before_tax_instance.save()
                    tax_instance = Tax(**{
                        'financial_year_id': int(form_data.get('year')),
                        'month': form_data.get('month'),
                        'tax_percentage': form_data.get('tax', 1.0)
                    })
                    tax_instance.save()
                    net_profit_instance = NetProfit(**{
                        'financial_year_id': int(form_data.get('year')),
                        'month': form_data.get('month')
                    })
                    net_profit_instance.save()
                if not isinstance(product_instance, QuerySet) and int(form_data.get('month')) == 0:
                    for month in MONTHS[2:]:
                        try:
                            revenue_instance = Revenue(**{
                                'product': product_instance,
                                'financial_year_id': int(form_data.get('year')),
                                'month': month[0]
                            })
                            revenue_instance.save()
                            gross_profit_instance = GrossProfit(**{
                                'product': product_instance,
                                'financial_year_id': int(form_data.get('year')),
                                'month': form_data.get('month'),
                                'cost_of_sale_id': cost_of_sale_instance.filter(product=product_instance).first().id
                            })
                            gross_profit_instance.save()
                        except Exception as ex:
                            pass
                    for month in MONTHS[2:]:
                        profit_before_tax_instance = ProfitBeforeTax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0]
                        })
                        profit_before_tax_instance.save()
                    for month in MONTHS[2:]:
                        tax_instance = Tax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0],
                            'tax_percentage': form_data.get('tax', 1.0)
                        })
                        tax_instance.save()
                    for month in MONTHS[2:]:
                        net_profit_instance = NetProfit(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0]
                        })
                        net_profit_instance.save()
                if not isinstance(product_instance, QuerySet) and int(form_data.get('month')) != 0:
                    try:
                        revenue_instance = Revenue(**{
                            'product': product_instance,
                            'financial_year_id': int(form_data.get('year')),
                            'month': form_data.get('month')
                        })
                        revenue_instance.save()
                        gross_profit_instance = GrossProfit(**{
                            'product': product_instance,
                            'financial_year_id': int(form_data.get('year')),
                            'month': form_data.get('month'),
                            'cost_of_sale_id': cost_of_sale_instance.filter(product=product_instance).first().id
                        })
                        gross_profit_instance.save()
                        profit_before_tax_instance = ProfitBeforeTax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': form_data.get('month')
                        })
                        profit_before_tax_instance.save()
                        tax_instance = Tax(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': form_data.get('month'),
                            'tax_percentage': form_data.get('tax', 1.0)
                        })
                        tax_instance.save()
                        net_profit_instance = NetProfit(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': form_data.get('month')
                        })
                        net_profit_instance.save()
                    except Exception as ex:
                        pass
                return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
            except (KeyError, AttributeError, Product.DoesNotExist, ProductSeasonalityRampUp.DoesNotExist, CostOfSale.DoesNotExist) as ex:
                form = GenerateRevenuePrediction(request.POST)
                return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
    else:
        form = GenerateRevenuePrediction()
        # response = html_to_pdf_creator()
        # return response
    return render(request, 'revenues/revenue.html', {'form': form, 'action': 'generate'})

