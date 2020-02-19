from itertools import groupby


class AppEngine(object):
    
    @classmethod
    def generate_report_data(cls):
        data = dict()
        from revenues.models import Revenue, Sale
        products = list(Sale.objects.values_list('product', flat=True).distinct())
        revenues = Revenue.objects.filter(product_id__in=products).order_by('id')
        product_revenues = revenues.values_list('id', 'product__name', 'financial_year', 'month', 'product_revenue')
        sorted_product_revenues = sorted(product_revenues, key=lambda x: x[1])
        grouped_product_revenues = groupby(sorted_product_revenues, key=lambda x: x[1])
        groups = dict()
        for product_name, product_revenues in grouped_product_revenues:
            groups[product_name] = list(product_revenues)
        data['revenues'] = groups
        product_sales = Sale.objects.filter(product_id__in=products).values_list(
            'product__name',
            'period',
            'total_sale_revenue'
        )
        sorted_product_sales = sorted(product_sales, key=lambda x: x[0])
        grouped_product_sales = groupby(sorted_product_sales, key=lambda x: x[0])
        groups = dict()
        for product_name, product_sales in grouped_product_sales:
            groups[product_name] = list(product_sales)
        data['sales'] = groups
        
        return data
