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


class ProductSeasonality (models.Model) :
    seasonality_description = models.CharField (max_length = 50)
    month_1_seasonality =  models.FloatField ( default = 0.083)
    month_2_seasonality =  models.FloatField ( default = 0.083)
    month_3_seasonality =  models.FloatField ( default = 0.083)
    month_4_seasonality =  models.FloatField ( default = 0.083)
    month_5_seasonality =  models.FloatField ( default = 0.083)
    month_6_seasonality =  models.FloatField ( default = 0.083)
    month_7_seasonality =  models.FloatField ( default = 0.083)
    month_8_seasonality =  models.FloatField ( default = 0.083)
    month_9_seasonality =  models.FloatField ( default = 0.083)
    month_10_seasonality =  models.FloatField ( default = 0.083)
    month_11_seasonality =  models.FloatField ( default = 0.083)
    month_12_seasonality =  models.FloatField ( default = 0.083)        


    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')
        
    def  __str__(self) :
        return self.seasonality_description
        