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
class CapacityRampUp (models.Model) :
        capacity_ramp_up_description = models.CharField (max_length = 50)
        month_1_ramp_up = models.FloatField ( default = 1.0)
        month_2_ramp_up = models.FloatField ( default = 1.0)
        month_3_ramp_up = models.FloatField ( default = 1.0)
        month_4_ramp_up = models.FloatField ( default = 1.0)
        month_5_ramp_up = models.FloatField ( default = 1.0)
        month_6_ramp_up = models.FloatField ( default = 1.0)
        month_7_ramp_up = models.FloatField ( default = 1.0)
        month_8_ramp_up = models.FloatField ( default = 1.0)
        month_9_ramp_up = models.FloatField ( default = 1.0)
        month_10_ramp_up = models.FloatField ( default = 1.0)
        month_11_ramp_up = models.FloatField ( default = 1.0)
        month_12_ramp_up = models.FloatField ( default = 1.0)


        def get_absolute_url(self):
                return reverse('businessplan:RevenueInput')
        
        def  __str__(self) :
                return self.capacity_ramp_up_description