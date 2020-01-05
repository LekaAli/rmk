from django.db import models
from dates.models import FinancialYear

MONTHS = (
        (0, '---Select Month---'),
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
TYPE = (
        (-1, '---Select Type---'),
        (0, 'For Many Products'),
        (1, 'For One Product')
    )


class SeasonalityValue(models.Model):
    
    month = models.PositiveSmallIntegerField(null=True, blank=True, choices=MONTHS)
    percentage = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
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
        return ''.join([v for k, v in self.MONTHS if k == self.month])

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
