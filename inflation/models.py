from django.db import models
from django.contrib.auth.models import User
from _datetime import datetime
import calendar
from django.db.models import Sum, Avg, F, Func
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import math
from django.utils.timezone import now
from django.urls import reverse


class Inflation(models.Model):
    description = models.CharField(max_length=50)
    value = models.FloatField(default=1.06)
    year = models.CharField(max_length=4, default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inflation'
        verbose_name_plural = 'Inflations'

    def save(self, *args, **kwargs):
        super(Inflation, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')
        
    def __str__(self):
        return self.description
