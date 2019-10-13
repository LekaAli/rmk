from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


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
    month = models.PositiveSmallIntegerField(blank=True, null=True, choices=MONTHS)
    percentage = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product RampUp'
        verbose_name_plural = 'Product RampUp'

    def projection_within_f_year(self):
        start_month = self.product.financial_year.start_date.month
        end_month = self.product.financial_year.end_date.month
        f_year_months = [month for month in range(start_month, 13, 1)]
        end = [month for month in range(1, end_month + 1, 1)]
        f_year_months.extend(end)
        return f_year_months

    def clean(self):
        allocated_months = ProductRampUp.objects.filter(product_id=self.product.id).values_list('month', flat=True)
        if len(allocated_months) == 0:
            if self.month != self.product.projection_start:
                raise ValidationError({
                    'month': 'Product starting ramp up should be %s' % self.product.projection_start
                })
        f_year_months = self.projection_within_f_year()
        if self.month not in f_year_months:
            raise ValidationError({
                'month': 'Month not within the financial year bounds'
            })

    def save(self, *args, **kwargs):

        super(ProductRampUp, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')

    def __str__(self):
        return '%s: %s' % (self.month, self.percentage)
