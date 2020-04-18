from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from revenues.models import Revenue
from revenues.forms import GenerateRevenuePrediction
from products.models import Product, ProductSeasonalityRampUp, CostOfSale, GrossProfit, ProfitBeforeTax, Tax, NetProfit
from django.db.models.query import QuerySet
from rmkplatform.constants import MONTHS
from dates.models import FinancialYear
from seasonality.models import SeasonalityValue
from rampup.models import RampUpValue
from utils.pdf_creator import html_to_pdf_creator


class RevenueInput(CreateView):
    model = Revenue
    template_name = 'revenues/revenue.html'
    fields = '__all__'


def pre_product_projection_check(product_instances, projection_data):
    products = list()
    for product_instance in product_instances:
        if projection_data['month'] not in ['0', 0]:
            revenue_instance = Revenue.objects.filter(
                product=product_instance,
                financial_year_id=int(projection_data['year']),
                month=int(projection_data['month'])
            )
            if not revenue_instance:
                products.append(product_instance)
            continue
        else:
            month_count = 0
            f_year_instance = FinancialYear.objects.filter(id=int(projection_data['year']))
            for month in MONTHS[:2]:
                revenue_instance = Revenue.objects.filter(
                    product=product_instance,
                    financial_year_id=int(projection_data['year']),
                    month=month[0]
                )
                if not revenue_instance:
                    month_count = month_count + 1
            if month_count > 0:
                products.append(product_instance)
    return products


def generate_revenue_projection(request):
    if request.method == 'POST':
        form = GenerateRevenuePrediction(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                if int(form_data['product']) != 0:  # projection for a given product
                    product_instance = Product.objects.filter(id=form_data['product'])
                else:  # projection for all available products
                    product_instance = Product.objects.all()

                seasonality_assignment = SeasonalityValue.objects.filter(
                    product__in=product_instance
                )
                rampup_assignment = RampUpValue.objects.filter(
                    product__in=product_instance
                )
                cost_of_sale_instance = CostOfSale.objects.filter(
                    product_id__in=product_instance.values_list('id', flat=True)
                )
                if product_instance:
                    # check if seasonality and ramp up values are assigned.
                    if seasonality_assignment.count() == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    if rampup_assignment.count() == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                else:
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                
                if isinstance(cost_of_sale_instance, CostOfSale):
                    if product_instance is None:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                elif isinstance(cost_of_sale_instance, QuerySet):
                    if len(cost_of_sale_instance) == 0:
                        return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                else:
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                    
                # all checks succeeded, perform revenue projections.
                # require: product, financial year & month
                # check financial year
                if not form_data.get('year'):
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                if not form_data.get('month'):
                    return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
                
                if isinstance(product_instance, QuerySet) and int(form_data.get('month')) == 0:
                    #  only project for products not already projected
                    product_instance = pre_product_projection_check(product_instance, form_data)
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
                            'tax_percentage': form_data.get('tax', 15.0)
                        })
                        tax_instance.save()
                    for month in MONTHS[2:]:
                        net_profit_instance = NetProfit(**{
                            'financial_year_id': int(form_data.get('year')),
                            'month': month[0] if isinstance(month, tuple) else month
                        })
                        net_profit_instance.save()
                if isinstance(product_instance, QuerySet) and int(form_data.get('month')) != 0:
                    #  only project for products not already projected
                    product_instance = pre_product_projection_check(product_instance, form_data)
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
                    #  only project for products not already projected
                    product_instance = pre_product_projection_check(product_instance, form_data)
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
                    #  only project for products not already projected
                    product_instance = pre_product_projection_check(product_instance, form_data)
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
                return render(
                    request,
                    'dates/success.html',
                    {
                        'form': form,
                        'btn_name': 'Another Projection',
                        'message': 'Projection was successful',
                        'action': 'update',
                        'view': 'revenue',
                    }
                )
            except (KeyError, AttributeError, Product.DoesNotExist, ProductSeasonalityRampUp.DoesNotExist, CostOfSale.DoesNotExist) as ex:
                form = GenerateRevenuePrediction(request.POST)
                return render(request, 'revenues/revenue.html', {'form': form, 'errors': ''})
    else:
        form = GenerateRevenuePrediction()
        
    return render(request, 'revenues/revenue.html', {'form': form, 'action': 'generate'})


def view_revenue_projection(request):
    response = html_to_pdf_creator()
    return response
