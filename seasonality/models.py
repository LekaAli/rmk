from django.db import models
from dates.models import FinancialYear
from rmkplatform.constants import MONTHS, TYPE


class SeasonalityValue(models.Model):
    financial_year = models.ForeignKey(FinancialYear, related_name='seasonality_f_year', on_delete=models.CASCADE, null=True,
                                       blank=True)
    month = models.PositiveSmallIntegerField(null=True, blank=True, choices=MONTHS)
    percentage = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    product = models.ManyToManyField('products.Product', related_name='product_seasonality', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Seasonality Value'
        verbose_name_plural = 'Seasonality Values'

    @property
    def month_percentage(self):
        return float(self.percentage) / 100

    @property
    def month_name(self):
        return ''.join([v for k, v in MONTHS if k == self.month])

    def __str__(self):
        return '%s - %s' % (self.month_name, self.percentage)


class Seasonality(models.Model):
    
    name = models.CharField(max_length=50, blank=True, null=True, help_text="Name to distinguish seasonalities.")
    seasonality_type = models.PositiveSmallIntegerField(
        choices=TYPE, blank=True, null=True, help_text="Seasonality type to be used.")
    seasonality_values = models.ManyToManyField(SeasonalityValue, related_name='seasonality_values', blank=True)
    year = models.ForeignKey(FinancialYear, related_name='seasonality_type', on_delete=models.CASCADE, blank=True, null=True)
    will_roll_over = models.BooleanField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Seasonality'
        verbose_name_plural = 'Seasonalities'

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.seasonality_type, self.year)
