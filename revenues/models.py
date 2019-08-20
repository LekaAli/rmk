from django.db import models
from django.contrib.auth.models import User
import datetime
from monthdelta import monthdelta
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
import math
from django.urls import reverse
from products.models import Product
from seasonality.models import ProductSeasonality
from rampup.models import CapacityRampUp
from seasonality.models import ProductSeasonality
from django.db.models import F


# class Revenue(models.Model) :
#     average_revenue_per_month = models.ManyToManyField(Product)
#     month_1_ramp_up = models.ManyToManyField(CapacityRampUp)
#     month_1_seasonality = models.ManyToManyField(ProductSeasonality)
#     #month_1_seasonality = models.ForeignKey(ProductSeasonality, on_delete=models.CASCADE)
#     month_1_revenue = models.FloatField (blank=True)
#
#     @property
#     def _get_total(self):
#             #functions to calculate whatever you want...
#         return self.average_revenue_per_month * self.month_1_ramp_up * self.month_1_seasonality
#
#     def save (self, *args, **kwargs):
#         self.month_1_revenue = self._get_total
#         super(Revenue, self).save(self, *args, **kwargs)
    
class Revenue(models.Model):
    product = models.ForeignKey(Product, related_name='product_revenue', on_delete=models.CASCADE, null=True, blank=True)
    seasonality = models.ForeignKey(ProductSeasonality, related_name='seasonalityrevenue', on_delete=models.CASCADE, blank=True, null=True)
    product_revenue = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Revenue'
        verbose_name_plural = 'Products Revenue'

    def save(self, *args, **kwargs):
        super(Revenue, self).save(self, *args, **kwargs)

    def __str__(self):
        return 'Month: %s, Product: %s, Revenue: R %s'.format(self.seasonality, self.product, self.product_revenue)