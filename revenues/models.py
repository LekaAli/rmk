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
from products.models import Products
from rampup.models import CapacityRampUp
from seasonality.models import ProductSeasonality
from django.db.models import F

# Create your models here.
class Revenue (models.Model) :
    average_revenue_per_month = models.ManyToManyField(Products)
    month_1_ramp_up = models.ManyToManyField(CapacityRampUp)
    month_1_seasonality = models.ManyToManyField(ProductSeasonality)
    #month_1_seasonality = models.ForeignKey(ProductSeasonality, on_delete=models.CASCADE)
    month_1_revenue = models.FloatField (blank=True)


    @property
    def _get_total(self):
            #functions to calculate whatever you want...
        return self.average_revenue_per_month * self.month_1_ramp_up * self.month_1_seasonality
   
    def save (self, *args, **kwargs):
        self.month_1_revenue = self._get_total
        super(Revenue, self).save(self, *args, **kwargs)
    
 