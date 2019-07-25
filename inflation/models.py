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
class Inflation (models.Model) :
    inflation_description = models.CharField (max_length = 50)
    year_2_inflation =  models.FloatField ( default = 1.06)
    year_3_inflation =  models.FloatField ( default = 1.06)
    year_4_inflation =  models.FloatField ( default = 1.06)
    year_5_inflation =  models.FloatField ( default = 1.06)
    year_6_inflation =  models.FloatField ( default = 1.06)
    year_7_inflation =  models.FloatField ( default = 1.06)
    year_8_inflation =  models.FloatField ( default = 1.06)
    year_9_inflation =  models.FloatField ( default = 1.06)
    year_10_inflation =  models.FloatField ( default = 1.06)

 
    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')
        
    def  __str__(self) :
        return self.inflation_description