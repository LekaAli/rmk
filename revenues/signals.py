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


class signals (models.Model):

    @receiver(post_save, sender=Products)
     
    def create_average_revenue_per_month (sender, instance, **kwargs):
        if created:
            Products.objects.create(Products=instance)
      
    
    def save_average_revenue_per_month(sender, instance, **kwargs):
        # month_1_revenue = Products.average_revenue_per_month(Products=instance)
        #month_1_revenue = CapacityRampUp.objects.get(CapacityRampUp=instance)
        #month_1_revenue = ProductSeasonality.objects.get(ProductSeasonality=instance)
        #month_1_revenue = F('average_revenue_per_month') * F('month_1_ramp_up')* F('month_1_seasonality')
        instance.average_revenue_per_month.save()
        #instance.month_1_seasonality.save()
        #instance.month_1_ramp_up.save()

        post_save.connect(safe_average_revenue_per_month, sender = Products)
    
    #ProductSeosenanality

    @receiver(post_save, sender=ProductSeasonality)

    def create_month_1_seasonality (sender, instance, **kwargs):
        if created:
            ProductSeasonality.objects.create(ProductSeasonality=instance)
      

    def save_month_1_seasonality (sender, instance, **kwargs):
        instance.month_1_seasonality.save()

        post_save.connect(save_month_1_seasonality, sender = ProductSeasonality)

    
    # CapacityRampU
    
    @receiver(post_save, sender=CapacityRampUp)
    
    def save_month_1_ramp_up (sender, instance, **kwargs):
        if created:
            ProductSeasonality.objects.create(CapacityRampUp=instance)
    
    
    
    def save_month_1_ramp_up (sender, instance, **kwargs):
        instance.month_1_ramp_up.save()

        post_save.connect(save_month_1_ramp_up, sender = CapacityRampUp)
    
    #def revenue_per_month(self, sender, instance, created, **kwargs):
     #   return ProductSeasonality.month_1_seasonality * CapacityRampUp.month_1_ramp_up * Products.average_revenue_per_month
             

   #m2m_changed.connect(revenue_per_month, sender=ProductSeasonality.month_1_seasonality)
    #m2m_changed.connect(revenue_per_month, sender=CapacityRampUp.month_1_ramp_up)
    #m2m_changed.connect(revenue_per_month, sender=Products.average_revenue_per_month)