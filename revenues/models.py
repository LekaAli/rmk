from django.db import models
from django.contrib.auth.models import User
from _datetime import datetime
from django.utils import timezone
from monthdelta import monthdelta
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
import math
from django.urls import reverse
from products.models import Product, Sale
from seasonality.models import ProductSeasonality
from inflation.models import Inflation
from rampup.models import ProductRampUp
from django.db.models import F


class ProductRevenue(models.Model):
    product = models.ForeignKey(Product, related_name='revenue_product', on_delete=models.CASCADE, null=True, blank=True)
    product_seasonality = models.ForeignKey(ProductSeasonality, related_name='revenue_product_seasonality', on_delete=models.CASCADE, blank=True, null=True)
    product_rampup = models.ForeignKey(ProductRampUp, related_name='revenue_product_rampup', on_delete=models.CASCADE, blank=True, null=True)
    inflation = models.FloatField(default=0)
    product_revenue = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Revenue'
        verbose_name_plural = 'Products Revenue'

    def save(self, *args, **kwargs):
        current_date = datetime.now(timezone.utc)
        product_longevity = current_date - self.product.created
        product_longevity_days = product_longevity.days
        product_longevity_days = 400
        year = float(product_longevity_days) / 365
        if year <= 1:  # year 1
            self.product_revenue = self.product.average_revenue_per_month * self.product_seasonality.demand_percentage * self.product_rampup.percentage
        elif 1 < year <= 2:
            inf = Inflation.objects.filter(year=2).values_list('percentage', flat=True)
            inf = [i for i in inf if i is not None]
            inf_val = float(inf[0])
            self.inflation = inf_val
            self.product_revenue = self.product.average_revenue_per_month * (1 + inf_val) * self.product_seasonality.demand_percentage
        elif 2 < year <= 3:
            inf = Inflation.objects.filter(year__in=[2, 3]).values_list('percentage', flat=True)
            inf = [i for i in inf if i is not None]
            inf_val = sum(inf)
            self.inflation = inf_val
            self.product_revenue = self.product.average_revenue_per_month * (1 + inf_val) * 12
        else:
            inf_val = Inflation.objects.filter(year=int(year)).values_list('percentage', flat=True)
            inf = [i for i in inf_val if i is not None]
            if len(inf) > 0:
                inf_val = inf[0]
            else:
                inf_val = 0
            self.inflation = inf_val
            self.product_revenue = self.product.average_revenue_per_month * (1 + inf_val) * 12
        # super(ProductRevenue, self).save(self, *args, **kwargs)
        # determine product longevity
        # determine which sale year class to update or create
        # - if year class is none, create a new one and set total sale value to product_revenue.
        # - if year class is not none, add product_revenue to the total sale value.
        year = int(year)
        product_sale = Sale.objects.filter(product_id=self.product.id, period=year)
        if product_sale.count() == 0:  # Year class is None
            product_sale = Sale.objects.create(**{
                'product': self.product,
                'total_sale_revenue': self.product_revenue,
                'period': year
            })
            product_sale.save()
        else:  # Year class is not None
            product_sale = product_sale.first()
            product_sale.total_sale_revenue = product_sale.total_sale_revenue + self.product_revenue
            product_sale.save()

    def __str__(self):
        return '%s' % self.product_revenue
