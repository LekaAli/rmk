from itertools import groupby


class AppEngine(object):
    
    @classmethod
    def generate_report_data(cls):
        data = dict()
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
        sorted_product_revenues = sorted(product_revenues, key=lambda x: x[1])
        grouped_product_revenues = groupby(sorted_product_revenues, key=lambda x: x[1])
        groups = dict()
        for product_name, product_revenues in grouped_product_revenues:
            processed_product_revenues = list()
            for product_revenue in product_revenues:
                product_revenue = list(product_revenue)
                product_revenue[3] = month_dict.get(product_revenue[3])[:3]
                processed_product_revenues.append(product_revenue)
            processed_product_revenues = groupby(processed_product_revenues, key=lambda x:x[2])
            processed_product = dict()
            for year, revenue in processed_product_revenues:
                processed_product[year] = list(revenue)
            groups[product_name] = processed_product
        
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
