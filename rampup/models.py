from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from dates.models import FinancialYear


class ProductRampUp(models.Model):
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
    product = models.ForeignKey('products.Product', related_name='product_rampup', on_delete=models.CASCADE, blank=True, null=True)
    financial_year = models.ForeignKey(FinancialYear, related_name='rampup_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(blank=True, null=True, choices=MONTHS)
    demand_value = models.PositiveSmallIntegerField(default=0)
    demand_percentage = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product RampUp'
        verbose_name_plural = 'Product RampUp'

    def projection_within_f_year(self):
        start_month = self.financial_year.start_date.month
        end_month = self.financial_year.end_date.month
        f_year_months = [month for month in range(start_month, 13, 1)]
        end = [month for month in range(1, end_month + 1, 1)]
        f_year_months.extend(end)
        return f_year_months

    def clean(self):
        allocated_months = ProductRampUp.objects.filter(product_id=self.product.id,financial_year=self.financial_year.id).values_list('month', flat=True)
        if len(allocated_months) == 0:
            if self.month != self.product.projection_start:
                raise ValidationError({
                    'month': 'Product starting ramp up should start on month %s' % self.product.projection_start
                })
        f_year_months = self.projection_within_f_year()
        diff = allocated_months[0] - f_year_months[0] if allocated_months[0] > f_year_months[0] else 0
        if len(allocated_months) == len(f_year_months[diff:]) and self.pk is None:
            raise ValidationError({
                'month': 'Ramp up projection fall outside financial year bounds'
            })

    def save(self, *args, **kwargs):
        self.demand_percentage = self.demand_value / 100
        super(ProductRampUp, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')

    def _model_instance_name(self, f_year, month, demand):
        name = ''.join([m[1] for m in self.MONTHS if m[0] == month])
        return '%s: %s: %s' % (f_year.description if f_year is not None else '', name, demand)

    def __str__(self):
        return self._model_instance_name(self.financial_year, self.month, self.demand_percentage)
