from django.db import models
# from django.contrib.auth.models import User
# from monthdelta import monthdelta
# import calendar
# from django.db.models import Sum, Avg, F, Func
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db.models.signals import pre_save, post_save
#
# from django.dispatch import receiver
# import math
from django.urls import reverse
from datetime import datetime
from seasonality.models import ProductSeasonality
from inflation.models import Inflation


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    average_unit_price = models.FloatField(default=10)
    average_quantity_per_month = models.FloatField(default=1.00)
    average_revenue_per_month = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def _get_total(self):
        return self.average_quantity_per_month * self.average_unit_price
   
    def save(self, *args, **kwargs):
        self.average_revenue_per_month = self._get_total
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
            
    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sale_price', on_delete=models.CASCADE, blank=True, null=True)
    ramp_up_capacity = models.FloatField(default=0.0)
    seasonality = models.ForeignKey(ProductSeasonality, related_name='sale_seasonality', on_delete=models.CASCADE, blank=True, null=True)
    inflation = models.ForeignKey(Inflation, related_name='sale_inflation', on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def save(self, *args, **kwargs):
        current_date = datetime.now()
        product_longevity = current_date - self.product.auto_created
        product_longevity_days = product_longevity.days
        if product_longevity_days <= 365:
            self.value = self.product.average_unit_price * self.seasonality.capacity * self.ramp_up_capacity
        elif 365 < product_longevity_days <= 356 * 2:
            self.value = self.product.average_unit_price * self.seasonality.capacity * self.inflation.value
        elif 365 * 2 < product_longevity_days <= 365 * 3:
            self.value = self.product.average_unit_price * self.inflation.value * 0.1 * 12
        super(Sale, self).save(*args, *kwargs)

    def __str__(self):
        return self.product