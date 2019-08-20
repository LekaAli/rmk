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


class ProductSeasonality(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    capacity = models.FloatField(default=0.083)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Seasonality'
        verbose_name_plural = 'Product Seasonalities'

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')
        
    def __str__(self):
        return self.name
