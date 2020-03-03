from itertools import groupby


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
    def generate_report_data(cls):
        
        from revenues.models import Revenue, Sale
        month_dict = {key: value for key, value in sorted(Revenue.MONTHS, key=lambda x: x[0])}
        products = list(Sale.objects.values_list('product', flat=True).distinct())
        revenues = Revenue.objects.filter(product_id__in=products).order_by('id')
        product_revenues = revenues.values_list(
            'id',
            'product__name',
            'financial_year__description',
            'month',
            'product_revenue'
        )
        sorted_by_year = sorted(product_revenues, key=lambda revenue_instance: revenue_instance[2])
        grouped_by_year = groupby(sorted_by_year, lambda revenue_instance: revenue_instance[2])
        data = {
            'monthly_revenue_total': dict(),
            'monthly_revenues': dict(),
            'yearly_revenues': dict(),
            'monthly_total_summation': dict(),
            'months': dict(),
            'cost_of_sale': dict(),
            'monthly_cost_of_sale_total': dict()
        }
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
            for month, month_revenue in grouped_by_month:
                month_revenue = list(month_revenue)
                month_revenue_total = {
                    '%s' % month_dict.get(month): sum(list(map(lambda x: x[4], month_revenue)))
                }
                month_cost_of_sale_total = {
                    '%s' % month_dict.get(month): sum(list(map(cls.calc_cost_of_sale, month_revenue)))
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
            cost_of_sale_dict = dict()
            for product_name, product_revenue_lst in grouped_by_products:
                product_revenue_lst = list(product_revenue_lst)
                products_dict[product_name] = product_revenue_lst
                cost_of_sale_dict.update({'%s' % product_name: list(map(cls.calc_cost_of_sale, product_revenue_lst))})
            data['monthly_revenues'][year_name] = products_dict
            data['cost_of_sale'][year_name] = cost_of_sale_dict
            data['yearly_revenues'].update({year_name: dict()})
            for product_name, product_revenue in products_dict.items():
                data['yearly_revenues'][year_name].update(
                    {
                        product_name: sum(
                            list(
                                map(lambda x: x[4], product_revenue)
                            )
                        )
                    }
                )
        
        return data
