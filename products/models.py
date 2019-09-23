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
from datetime import datetime, timezone
# from revenues.models import ProductRevenue


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
    total_sale_revenue = models.FloatField(default=0.00)
    period = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Sale'
        verbose_name_plural = 'Product Sales'

    def save(self, *args, **kwargs):
        from revenues.models import ProductRevenue
        product_revenue = ProductRevenue.objects.filter(product_id=self.product.id)
        self.total_sale_revenue = sum([p_revenue for p_revenue in product_revenue.values_list('product_revenue', flat=True) if p_revenue is not None])
        current_date = datetime.now(timezone.utc)
        product_longevity = current_date - self.product.created
        product_period = int(float(product_longevity.days) / 365)
        self.period = 0 if product_period < 1 else product_period
        super(Sale, self).save(*args, *kwargs)

    def __str__(self):
        return '%s: %.2f' % (self.product.name, self.total_sale_revenue)
