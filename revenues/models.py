from django.db import models
from products.models import Product, Sale
from dates.models import FinancialYear
from seasonality.models import ProductSeasonality
from rampup.models import ProductRampUp


class ProductRevenue(models.Model):
    product = models.ForeignKey('products.Product', related_name='revenue_product', on_delete=models.CASCADE, null=True, blank=True)
    product_seasonality = models.ForeignKey(ProductSeasonality, related_name='revenue_product_seasonality', on_delete=models.CASCADE, blank=True, null=True)
    product_rampup = models.ForeignKey(ProductRampUp, related_name='revenue_product_rampup', on_delete=models.CASCADE, blank=True, null=True)
    inflation = models.FloatField(default=0)
    month = models.PositiveSmallIntegerField(default=1)
    financial_year = models.ForeignKey(FinancialYear, related_name='revenue_f_year', on_delete=models.CASCADE, blank=False, null=True)
    product_revenue = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Revenue'
        verbose_name_plural = 'Products Revenue'

    def save(self, *args, **kwargs):

        product_years = ProductSeasonality.objects.filter(product_id=self.product.id).values_list('financial_year', flat=True).distinct()
        self.inflation = self.product_seasonality.financial_year.inflation
        year_count = product_years.count()
        if len(product_years) in [0, 1]:
            self.product_revenue = self.product.average_revenue_per_month * self.product_seasonality.demand_percentage * self.product_rampup.percentage
            # self.period = 1
        elif len(product_years) == 2:
            self.product_revenue = self.product.average_revenue_per_month * (
                        1 + self.inflation) * self.product_seasonality.demand_percentage
            # self.period = 2
        elif len(product_years) == 3:
            self.product_revenue = self.product.average_revenue_per_month * (1 + self.inflation) * 12
            # self.period = 3
        else:
            past_year = year_count - 1
            past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_year)
            self.product_revenue = past_year_revenue.total_sale_revenue * (1 + self.inflation)
            # self.period = year_count

        product_sale = Sale.objects.filter(product_id=self.product.id, period=year_count)
        if len(product_sale) == 0:
            product_sale = Sale(product_id=self.product.id, period=year_count)
            product_sale.total_sale_revenue = self.product_revenue
            product_sale.save()
        else:
            product_sale = product_sale.first()

            if not self.pk:
                product_sale.total_sale_revenue = product_sale.total_sale_revenue + self.product_revenue
                product_sale.save()
        self.month = self.product_seasonality.month
        self.financial_year = self.product_seasonality.financial_year
        super(ProductRevenue, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.product_revenue
