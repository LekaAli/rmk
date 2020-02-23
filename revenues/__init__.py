from itertools import groupby


class AppEngine(object):
    
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
        data = {'monthly_revenue_total': dict(), 'monthly_revenues': dict(), 'yearly_revenues': dict()}
        for year_name, year_revenue_iter in grouped_by_year:
            data['monthly_revenues'].update({'%s' % year_name: list(year_revenue_iter)})
            sorted_by_month = sorted(
                data['monthly_revenues'].get(year_name),
                key=lambda year_revenue_instance: year_revenue_instance[3]
            )
            grouped_by_month = groupby(sorted_by_month, key=lambda year_revenue_instance: year_revenue_instance[3])
            for month, month_revenue in grouped_by_month:
                data['monthly_revenue_total'].update(
                    {
                        '%s' % month_dict.get(month): sum(
                            list(
                                map(lambda x: x[4], list(month_revenue))
                            )
                        )
                    }
                )
        data['months'] = [month[:3] for month in data['monthly_revenue_total'].keys()]
        data['monthly_total_summation'] = sum([month for month in data['monthly_revenue_total'].values()])
        for year_name, year_revenues in data['monthly_revenues'].items():
            sorted_by_products = sorted(year_revenues, key=lambda product_revenue_instance: product_revenue_instance[1])
            grouped_by_products = groupby(
                sorted_by_products, key=lambda product_revenue_instance: product_revenue_instance[1]
            )
            products_dict = dict()
            for product_name, product_revenue_lst in grouped_by_products:
                products_dict[product_name] = list(product_revenue_lst)
            data['monthly_revenues'][year_name] = products_dict
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
