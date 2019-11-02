from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from dates.models import FinancialYear
# from products.models import Product


class ProductSeasonality(models.Model):
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
    product = models.ForeignKey('products.Product', related_name='product_seasonality', on_delete=models.CASCADE, blank=True, null=True)
    financial_year = models.ForeignKey(FinancialYear, related_name='seasonality_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(null=True, blank=True, choices=MONTHS)
    demand_value = models.PositiveSmallIntegerField(default=0)
    demand_percentage = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Seasonality'
        verbose_name_plural = 'Product Seasonalities'

    def projection_within_f_year(self):
        start_month = self.financial_year.start_date.month
        end_month = self.financial_year.end_date.month
        f_year_months = [month for month in range(start_month, 13, 1)]
        end = [month for month in range(1, end_month + 1, 1)]
        f_year_months.extend(end)
        return f_year_months

    def clean(self):
        allocated_months = ProductSeasonality.objects.filter(product_id=self.product.id).values_list('month', flat=True)
        if len(allocated_months) == 0:
            if self.month != self.product.projection_start:
                raise ValidationError({
                    'month': 'Product starting seasonality should be %s' % self.product.projection_start
                })
        f_year_months = self.projection_within_f_year()
        if self.month not in f_year_months:
            raise ValidationError({
                'month': 'Month not within the financial year bounds'
            })

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')

    def save(self, *args, **kwargs):
        self.demand_percentage = float(self.demand_value) / 100 if self.demand_value is not None else 0.0
        super(ProductSeasonality, self).save(*args, **kwargs)

    def _model_instance_name(self, f_year, month, demand):
        name = ''.join([m[1] for m in self.MONTHS if m[0] == month])
        return '%s: %s: %s' % (f_year, name, demand)

    def __str__(self):
        return self._model_instance_name(self.financial_year.description, self.month, self.demand_percentage)

