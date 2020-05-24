from itertools import groupby
from rmkplatform.constants import MONTHS
from ast import literal_eval


class AppEngine(object):
    
    @classmethod
    def calc_cost_of_sale(cls, revenue_instance):
        from products.models import CostOfSale
        product_cost_of_sale = CostOfSale.objects.filter(product__name=revenue_instance[1])
        if product_cost_of_sale.count() > 0:
            val = product_cost_of_sale.first()
            return float(revenue_instance[4]) * val.percentage
        return revenue_instance[4]
    
    @classmethod
    def calc_profit_before_tax(cls, data, month_dict):
        from products.models import ProfitBeforeTax, Expense
        profit_before_taxes = ProfitBeforeTax.objects.values_list(
            'id',
            'financial_year__description',
            'month',
            'expense',
            'profit_before_tax',
        )

        sorted_profit_before_tax = sorted(profit_before_taxes, key=lambda profit_before_tax: profit_before_tax[1])
        grouped_profit_before_tax = groupby(
            sorted_profit_before_tax,
            key=lambda profit_before_tax: profit_before_tax[1]
        )
        grouped_expense_dict = dict()
        for year_name, profit_before_tax_yearly_iter in grouped_profit_before_tax:
            profit_before_tax_grouped_yearly_lst = list(profit_before_tax_yearly_iter)
            profit_before_tax_sorted_monthly_lst = sorted(
                profit_before_tax_grouped_yearly_lst, key=lambda yearly_profit_before_tax: yearly_profit_before_tax[2]
            )
            profit_before_tax_sorted_monthly_iter = groupby(
                profit_before_tax_sorted_monthly_lst, key=lambda yearly_profit_before_tax: yearly_profit_before_tax[2]
            )
            data['expenses'].update({year_name: dict()})
            data['profit_before_tax'].update({year_name: dict()})
            data['monthly_expense_total'].update({year_name: dict()})
            data['yearly_expense_total'].update({year_name: dict()})
            expense_months_dict = dict([(m, list(d)) for m, d in profit_before_tax_sorted_monthly_iter])
            for m_k, m_v in month_dict.items():
                p_b_tax_val = 0.0
                if m_k in expense_months_dict.keys():
                    vals = expense_months_dict[m_k][0]
                    e_val = literal_eval(vals[3])
                    p_b_tax_val = vals[4]
                else:
                    p_b_tax_instance = ProfitBeforeTax.objects.first()
                    d = literal_eval(p_b_tax_instance.expense)
                    for k, v in d.items():
                        for k1, v1 in v.items():
                            d[k][k1] = 0.0
                    e_val = d
                data['expenses'][year_name].update(
                    {
                        m_v: e_val
                    }
                )
                data['profit_before_tax'][year_name].update(
                    {
                        m_v: p_b_tax_val
                    }
                )
            grouped_expense_dict[year_name] = dict()
            for month, expense_dict in data['expenses'][year_name].items():
                if len(expense_dict) == 0:
                    data['monthly_expense_total'][year_name].update({'empty': dict()})
                    continue
                for expense_category_name, expense_value_dict in expense_dict.items():
                    if expense_category_name not in grouped_expense_dict[year_name].keys():
                        grouped_expense_dict[year_name].update({expense_category_name: dict()})
                        data['monthly_expense_total'][year_name].update({expense_category_name: dict()})
                        data['yearly_expense_total'][year_name].update({expense_category_name: dict()})
                    monthly_total = 0.0
                    for e_name, e_amount in expense_value_dict.items():
                        monthly_total = monthly_total + e_amount
                        if e_name in data['yearly_expense_total'][year_name][expense_category_name].keys():
                            data['yearly_expense_total'][year_name][expense_category_name][e_name] += e_amount
                        else:
                            data['yearly_expense_total'][year_name][expense_category_name][e_name] = e_amount
                        if e_name not in grouped_expense_dict[year_name][expense_category_name].keys():
                            grouped_expense_dict[year_name][expense_category_name][e_name] = {month: e_amount}
                        else:
                            grouped_expense_dict[year_name][expense_category_name][e_name].update({month: e_amount})
                    data['monthly_expense_total'][year_name][expense_category_name].update({month: monthly_total})
            for category, amount_dict in data['yearly_expense_total'][year_name].items():
                if category != 'empty':
                    data['yearly_expense_total'][year_name][category]['total'] = sum(amount_dict.values())
            data['expenses'] = grouped_expense_dict
    
    @classmethod
    def calc_tax(cls, data, month_dict):
        from products.models import Tax
        taxes = Tax.objects.values_list(
            'id',
            'financial_year__description',
            'month',
            'tax_percentage',
            'profit_loss_value',
            'total_tax_value'
        )
        sorted_taxes = sorted(taxes, key=lambda tax_instance: tax_instance[1])
        grouped_taxes = groupby(sorted_taxes, key=lambda tax_instance: tax_instance[1])
        for year, yearly_taxes_iter in grouped_taxes:
            year_taxes_lst = list(yearly_taxes_iter)
            sorted_monthly_taxes = sorted(year_taxes_lst, key=lambda tax_instance: tax_instance[2])
            grouped_monthly_taxes = groupby(sorted_monthly_taxes, key=lambda tax_instance: tax_instance[2])
            data['tax'].update({'%s' % year: dict()})
            monthly_taxes = dict([(k, list(v)) for k, v in grouped_monthly_taxes])
            for k, v in month_dict.items():
                if k in monthly_taxes.keys():
                    data['tax']['%s' % year].update({
                        month_dict.get(k): monthly_taxes[k][0][5]
                    })
                else:
                    data['tax']['%s' % year].update({
                        month_dict.get(k): 0.0
                    })
        
    @classmethod
    def calc_net_profit(cls, data, month_dict):
        from products.models import NetProfit
        net_profits = NetProfit.objects.values_list(
            'id',
            'financial_year__description',
            'month',
            'net_profit',
        )
        sorted_net_profits = sorted(net_profits, key=lambda net_profit_instance: net_profit_instance[1])
        grouped_net_profits = groupby(sorted_net_profits, key=lambda net_profit_instance: net_profit_instance[1])
        for year, yearly_net_profit_iter in grouped_net_profits:
            year_net_profits_lst = list(yearly_net_profit_iter)
            sorted_monthly_net_profits = sorted(year_net_profits_lst, key=lambda net_profit_instance: net_profit_instance[2])
            grouped_monthly_net_profits = groupby(sorted_monthly_net_profits, key=lambda net_profit_instance: net_profit_instance[2])
            data['net_profit'].update({'%s' % year: dict()})
            month_net_profit_dict = dict([(k, list(v)) for k, v in grouped_monthly_net_profits])
            for k, v in month_dict.items():
                if k in month_net_profit_dict.keys():
                    data['net_profit']['%s' % year].update({
                        month_dict.get(k): month_net_profit_dict[k][0][3]
                    })
                else:
                    data['net_profit']['%s' % year].update({
                        month_dict.get(k): 0.0
                    })

    @classmethod
    def generate_report_data(cls):
        
        from revenues.models import Revenue, Sale
        from products.models import GrossProfit
        month_dict = {key: value for key, value in sorted(Revenue.MONTHS, key=lambda x: x[0])}
        products = list(Sale.objects.values_list('product', flat=True).distinct())
        revenues = Revenue.objects.filter(product_id__in=products).order_by('id')
        gross_profits = GrossProfit.objects.filter(product_id__in=products).order_by('id')
        product_revenues = revenues.values_list(
            'id',
            'product__name',
            'financial_year__description',
            'month',
            'product_revenue'
        )
        product_gross_profit_cost_of_sale = gross_profits.values_list(
            'id',
            'product__name',
            'financial_year__description',
            'month',
            'cost_of_sale_value',
            'gross_profit_value'
        )
        sorted_gross_profit_cost_of_sale = sorted(product_gross_profit_cost_of_sale, key=lambda instance: instance[2])
        grouped_gross_profit_cost_of_sale = groupby(sorted_gross_profit_cost_of_sale, key=lambda instance: instance[2])
        sorted_by_year = sorted(product_revenues, key=lambda revenue_instance: revenue_instance[2])
        grouped_by_year = groupby(sorted_by_year, lambda revenue_instance: revenue_instance[2])
        data = {
            'monthly_revenue_total': dict(),
            'monthly_revenues': dict(),
            'yearly_revenues': dict(),
            'monthly_total_summation': dict(),
            'months': dict(),
            'cost_of_sale_total': dict(),
            'cost_of_sale': dict(),
            'monthly_cost_of_sale_total': dict(),
            'gross_profit_total': dict(),
            'expenses': dict(),
            'monthly_expense_total': dict(),
            'yearly_expense_total': dict(),
            'profit_before_tax': dict(),
            'tax': dict(),
            'net_profit': dict()
        }
        for year_name, year_gross_profit_cost_of_sale_iter in grouped_gross_profit_cost_of_sale:
            year_gross_profit_cost_of_sale = list(year_gross_profit_cost_of_sale_iter)
            sorted_year_gross_profit_cost_of_sale = sorted(
                year_gross_profit_cost_of_sale,
                key=lambda instance: instance[3]
            )
            grouped_year_gross_profit_cost_of_sale = groupby(
                sorted_year_gross_profit_cost_of_sale,
                key=lambda instance: instance[3]
            )
            data['cost_of_sale_total'].update({year_name: dict()})
            data['cost_of_sale'].update({year_name: dict()})
            data['gross_profit_total'].update({year_name: dict()})
            month_dict = {val[0]: val[1][:3] for val in MONTHS[2:]}
            gross_profit_dict = dict([(k, list(v)) for k, v in grouped_year_gross_profit_cost_of_sale])
            p_name = ''
            for k, v in month_dict.items():
                if k not in gross_profit_dict.keys():
                    data['gross_profit_total'][year_name].update({
                        '%s' % month_dict.get(k): 0.0
                    })
                    data['cost_of_sale_total'][year_name].update({
                        '%s' % month_dict.get(k): 0.0
                    })
                    data['cost_of_sale'][year_name][month_dict.get(k)] = {
                            p_name: 0.0
                        }
                else:
                    monthly_values = gross_profit_dict[k]
                    data['gross_profit_total'][year_name].update({
                        '%s' % month_dict.get(k): sum(list(map(lambda x: float(x[5]), monthly_values)))
                    })
                    data['cost_of_sale_total'][year_name].update({
                        '%s' % month_dict.get(k): sum(list(map(lambda x: float(x[4]), monthly_values)))
                    })
                    sorted_cost_of_sale = sorted(monthly_values, key=lambda instance: instance[1])
                    grouped_cost_of_sale = groupby(sorted_cost_of_sale, key=lambda instance: instance[1])

                    data['cost_of_sale'][year_name].update({month_dict.get(k): dict()})
                    for product_name, product_cost_of_sale_iter in grouped_cost_of_sale:
                        p_name = product_name
                        cost_of_sale_val = list(product_cost_of_sale_iter)
                        data['cost_of_sale'][year_name][month_dict.get(k)].update(
                            {
                                product_name: cost_of_sale_val[0][4]
                            }
                        )
        m_dict = dict([(k, v[:3]) for k, v in MONTHS[2:]])
        revenue_cos_dict = dict()
        for year_name, year_revenue_iter in grouped_by_year:
            year_revenue_lst = list(year_revenue_iter)
            data['monthly_revenues'].update({year_name: year_revenue_lst})
            sorted_by_month = sorted(
                year_revenue_lst,
                key=lambda year_revenue_instance: year_revenue_instance[3]
            )
            grouped_by_month = groupby(sorted_by_month, key=lambda year_revenue_instance: year_revenue_instance[3])
            data['monthly_revenue_total'].update({year_name: dict()})
            data['monthly_cost_of_sale_total'].update({year_name: dict()})
            
            for k, v in grouped_by_month:
                revenue_cos_dict.update({
                    k: list(v)
                })
            for m_k, m_v in m_dict.items():
                if m_k in revenue_cos_dict.keys():
                    month_revenue_total = {
                        '%s' % m_dict.get(m_k): float(sum(list(map(lambda x: x[4], revenue_cos_dict[m_k]))))
                    }
                    month_cost_of_sale_total = {
                        '%s' % m_dict.get(m_k): float(sum(list(map(cls.calc_cost_of_sale, revenue_cos_dict[m_k]))))
                    }
                else:
                    month_revenue_total = {
                        '%s' % m_dict.get(m_k): 0.0
                    }
                    month_cost_of_sale_total = {
                        '%s' % m_dict.get(m_k): 0.0
                    }
                data['monthly_revenue_total'][year_name].update(month_revenue_total)
                data['monthly_cost_of_sale_total'][year_name].update(month_cost_of_sale_total)
            data['monthly_total_summation'].update(
                {
                    year_name: sum(data['monthly_revenue_total'].get(year_name).values())
                }
            )
            data['months'].update(
                {
                    year_name: [month[:3] for month in data['monthly_revenue_total'].get(year_name).keys()]
                }
            )
        for year_name, year_revenues in data['monthly_revenues'].items():
            sorted_by_products = sorted(year_revenues, key=lambda product_revenue_instance: product_revenue_instance[1])
            grouped_by_products = groupby(
                sorted_by_products, key=lambda product_revenue_instance: product_revenue_instance[1]
            )
            products_dict = dict()
            month_dict = {val[0]: val[1][:3] for val in MONTHS[2:]}
            for product_name, product_revenue_iter in grouped_by_products:
                month_vals_lst = list(product_revenue_iter)
                months = [k[3] for k in month_vals_lst]
                for k, v in month_dict.items():
                    if k not in months:
                        product = 0, product_name, year_name, k, 0.0
                        month_vals_lst.append(product)
                    continue
                products_dict[product_name] = month_vals_lst
            data['monthly_revenues'][year_name] = products_dict
            data['yearly_revenues'].update({year_name: dict()})
            for product_name, product_revenue in products_dict.items():
                data['yearly_revenues'][year_name].update(
                    {
                        product_name: sum(
                            list(
                                map(lambda x: float(x[4]), product_revenue)
                            )
                        )
                    }
                )
            cls.calc_profit_before_tax(data, month_dict)
            cls.calc_tax(data, month_dict)
            cls.calc_net_profit(data, month_dict)
        return data

# <pdf:pagenumber> of <pdf:pagecount>