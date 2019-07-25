from django.db import models
from django.contrib.auth.models import User
import datetime
from monthdelta import monthdelta
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver
import math
from django.urls import reverse

# Create your models here.
class Products(models.Model) :
    product_name = models.CharField (max_length = 50)
    product_description = models.CharField (max_length = 50)
    average_unit_price = models.FloatField(default = 10)
    average_quantity_per_month = models.FloatField(default=1.00)
    average_revenue_per_month = models.FloatField(blank=True)

    @property
    def _get_total(self):
            #functions to calculate whatever you want...
        return self.average_quantity_per_month * self.average_unit_price
   
    def save (self, *args, **kwargs):
        self.average_revenue_per_month = self._get_total
        super(Products, self).save(self, *args, **kwargs)

    def __str__(self) :
        return self.product_name
            
    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput') 
