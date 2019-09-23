from django.db import models
from django.contrib.auth.models import User
import datetime
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import math
from django.urls import reverse
from products.models import Product


class ProductSeasonality(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    month = models.SmallIntegerField(null=True, blank=True)
    demand_value = models.PositiveSmallIntegerField(default=0)
    demand_percentage = models.FloatField(default=0.00)
    product = models.ForeignKey(Product, related_name='product_seasonality', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Seasonality'
        verbose_name_plural = 'Product Seasonalities'

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')

    def save(self, *args, **kwargs):
        if self.pk not in [None, '']:
            pass
        else:
            month = ProductSeasonality.objects.filter(product_id=self.product.id).values_list('month', flat=True)
            month = [m for m in month if m is not None]
            self.month = max(month) + 1 if len(month) > 0 else 1
        self.demand_percentage = float(self.demand_value) / 100 if self.demand_value is not None else 0.0
        super(ProductSeasonality, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.name, self.demand_percentage)
