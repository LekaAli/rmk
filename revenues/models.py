from django.db import models
from products.models import Product, Sale
from dates.models import FinancialYear
from seasonality.models import ProductSeasonality
from rampup.models import ProductRampUp


class ProductRevenue(models.Model):
    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )
    product = models.ForeignKey('products.Product', related_name='revenue_product', on_delete=models.CASCADE, null=True, blank=True)
    financial_year = models.ForeignKey(FinancialYear, related_name='revenue_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True)
    inflation = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    product_revenue = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Revenue'
        verbose_name_plural = 'Products Revenue'

    def save(self, *args, **kwargs):

        product_years = ProductSeasonality.objects.filter(
            product_id=self.product.id
        ).values_list(
            'financial_year',
            flat=True
        ).distinct()
        year_count = product_years.count()
        product_seasonality = ProductSeasonality.objects.filter(
            product_id=self.product.id,
            month=self.month,
            financial_year=self.financial_year.id
        ).first()
        product_rampup = ProductRampUp.objects.filter(
            product_id=self.product.id,
            month=self.month,
            financial_year=self.financial_year.id
        ).first()
        self.inflation = product_seasonality.financial_year.inflation
        self.financial_year = product_seasonality.financial_year
        self.month = product_seasonality.month
        if len(product_years) in [0, 1]:
            self.product_revenue = self.product.average_revenue_per_month * product_seasonality.demand_percentage * product_rampup.demand_percentage
        elif len(product_years) == 2:
            self.product_revenue = self.product.average_revenue_per_month * (
                    1 + self.inflation) * product_seasonality.demand_percentage
        elif len(product_years) == 3:
            self.product_revenue = self.product.average_revenue_per_month * (1 + self.inflation) * 12
        else:
            past_year = year_count - 1
            past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_year)
            self.product_revenue = past_year_revenue.first().total_sale_revenue * (1 + self.inflation)
        if len(product_years) < 3:
            product_sale = Sale.objects.filter(product_id=self.product.id, period=year_count, month=self.month)
            if len(product_sale) == 0:
                product_sale = Sale(product_id=self.product.id, period=year_count, month=self.month)
                product_sale.month_sale = self.product_revenue
                product_sale.save()
            else:
                product_sale = product_sale.first()
                if not self.pk:
                    product_sale.month_sale = product_sale.month_sale + self.product_revenue
                    product_sale.save()
        else:
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
        super(ProductRevenue, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.product_revenue
