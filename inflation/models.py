from django.db import models
from django.contrib.auth.models import User
from _datetime import datetime
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import math
from django.utils.timezone import now
from django.urls import reverse
from dates.models import FinancialYear


class Inflation(models.Model):
    description = models.CharField(max_length=50, help_text='Inflation description text')
    value = models.PositiveSmallIntegerField(help_text='Inflation value')
    percentage = models.DecimalField(max_digits=2, decimal_places=2, help_text='Inflation value iun percentages')
    financial_year = models.ForeignKey(FinancialYear, related_name='inflation_f_year', on_delete=models.CASCADE,
                                       blank=False, null=True)
    # year = models.PositiveSmallIntegerField(default=2, help_text='Inflation year value')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inflation'
        verbose_name_plural = 'Inflations'

    def save(self, *args, **kwargs):
        # if self.pk not in [None, '']:
        #     pass
        # else:
        #     inf = Inflation.objects.values_list('year', flat=True)
        #     max_year_val = max(inf) if len(inf) > 0 else 1
        #     self.year = max_year_val + 1
        self.percentage = float(self.value) / 100 if self.value is not None else 0
        super(Inflation, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')
        
    def __str__(self):
        return self.description
