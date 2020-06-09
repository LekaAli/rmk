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

class Promoter(models.Model):
        user = models.ForeignKey (User, on_delete=models.CASCADE)
        promoter_name =  models.CharField (max_length = 50)
        promoter_last_name = models.CharField (max_length = 50)
        promoter_date_of_birth = models.DateField(null=True)
        gender = models.CharField (max_length = 50)

        def get_absolute_url(self):
                return reverse('businessplan:BusinessDetails')

        def  __str__(self) :
                return self.promoter_name

class BusinessDetails(models.Model):
        promoter_name = models.ForeignKey (Promoter, on_delete=models.CASCADE)
        business_name = models.CharField (max_length = 50)  
        business_description =  models.CharField (max_length = 150)

    
        def  __str__(self) :
                return self.business_name

        def get_absolute_url(self):
                return reverse('dates:CreateDates')

            
       
    
