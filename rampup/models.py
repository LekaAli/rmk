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


class RampUpValue(models.Model):
    month = models.PositiveSmallIntegerField(null=True, blank=True, choices=MONTHS)
    percentage = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product RampUp Value'
        verbose_name_plural = 'Product RampUp Values'

    @property
    def month_percentage(self):
        return float(self.percentage) / 100

    @property
    def month_name(self):
        return ''.join([v for k, v in self.MONTHS if k == self.month])
    
    def __str__(self):
        return '%s - %s' % (self.month_name, self.percentage)


class RampUp(models.Model):
    
    name = models.CharField(max_length=50, blank=True, null=True, help_text="Name to distinguish ramp ups.")
    rampup_type = models.PositiveSmallIntegerField(
        choices=TYPE, blank=True, null=True, help_text="Ramp Up type to be used.")
    rampup_values = models.ManyToManyField(RampUpValue, related_name='rampup_values', blank=True)
    year = models.ForeignKey(FinancialYear, related_name='rampup_type', on_delete=models.CASCADE, blank=True, null=True)
    will_roll_over = models.BooleanField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Ramp Up'
        verbose_name_plural = 'Product Ramp Ups'

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.rampup_type, self.year)


