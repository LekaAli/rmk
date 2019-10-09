from django.db import models
# from django.contrib.auth.models import User
# from monthdelta import monthdelta
# import calendar
# from django.db.models import Sum, Avg, F, Func
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db.models.signals import pre_save, post_save
#
# from django.dispatch import receiver
# import math
from django.urls import reverse
from datetime import datetime, timezone
# from revenues.models import ProductRevenue
from dates.models import FinancialYear


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    projection_start = models.DateField(blank=False, null=True)
    financial_year = models.ForeignKey(FinancialYear, related_name='product_fin_year', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=50)
    average_unit_price = models.FloatField(default=10)
    average_quantity_per_month = models.FloatField(default=1.00)
    average_revenue_per_month = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @classmethod
    def projection_within_f_year(cls, value):
        pass

    @property
    def _get_total(self):
        return self.average_quantity_per_month * self.average_unit_price
   
    def save(self, *args, **kwargs):
        self.average_revenue_per_month = self._get_total
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
            
    def get_absolute_url(self):
        return reverse('businessplan:RevenueInput')


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sale_price', on_delete=models.CASCADE, blank=True, null=True)
    total_sale_revenue = models.FloatField(default=0.00)
    period = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Sale'
        verbose_name_plural = 'Product Sales'

    def save(self, *args, **kwargs):
        from revenues.models import ProductRevenue
        product_revenue = ProductRevenue.objects.filter(product_id=self.product.id)
        self.total_sale_revenue = sum([p_revenue for p_revenue in product_revenue.values_list('product_revenue', flat=True) if p_revenue is not None])
        current_date = datetime.now(timezone.utc)
        product_longevity = current_date - self.product.created
        product_period = int(float(product_longevity.days) / 365)
        self.period = 0 if product_period < 1 else product_period
        super(Sale, self).save(*args, *kwargs)

    def __str__(self):
        return '%s: %.2f' % (self.product.name, self.total_sale_revenue)


class GrossProfit(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    sale = models.ForeignKey(Sale, related_name='sale', on_delete=models.CASCADE, blank=True, null=True)
    cost_of_sale = models.FloatField(default=0.00)
    gross_profit_value = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gross Profit'
        verbose_name_plural = 'Gross Profits'

    def save(self, *args, **kwargs):
        self.gross_profit_value = self.product.sale - self.sale.cost_of_sale
        super(GrossProfit, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s = %s' % (self.product.sale, self.cost_of_sale, self.gross_profit)


class Expense(models.Model):
    sale = models.ForeignKey(Sale, related_name='expenses', on_delete=models.CASCADE, blank=True, null=True)
    is_fixed = models.BooleanField()
    value = models.FloatField()
    total = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def save(self, *args, **kwargs):
        super(Expense, self).save(*args, **kwargs)
        if self.is_fixed is True:
            self.total = self.sale - self.value
        else:
            self.total = self.sale - self.value * 0.1 * self.sale

    def __str__(self):
        return '%s percent of expenses' % self.value if self.is_fixed is True else '%s for expenses' % self.value


class ProfitBeforeTax(models.Model):
    gross = models.ForeignKey(GrossProfit, related_name='gross_profit', on_delete=models.CASCADE, blank=True, null=True)
    expense = models.ForeignKey(Expense, related_name='expense', on_delete=models.CASCADE, blank=True, null=True)
    total_value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profit Before Tax'
        verbose_name_plural = 'Profit Before Taxes'

    def save(self, *args, **kwargs):
        super(ProfitBeforeTax, self).save(*args, **kwargs)
        self.total_value = self.gross.gross_profit_value - self.expense

    def __str__(self):
        return ''


class Tax(models.Model):
    profit_before_tax = models.ForeignKey(ProfitBeforeTax, related_name='profit_before_tax', on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def save(self, *args, **kwargs):
        super(Tax, self).save(*args, **kwargs)
        if self.profit_before_tax.total_value < 0:
            pass
            # cover loss for previous years
        else:
            pass
            # calculate tax

    def __str__(self):
        return ''


class NetProfit(models.Model):
    tax = models.ForeignKey(Tax, related_name='tax', on_delete=models.CASCADE, blank=True, null=True)
    net_profit = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Net Profit'
        verbose_name_plural = 'Net Profits'

    def save(self, *args, **kwargs):
        super(NetProfit, self).save(*args, **kwargs)
        self.net_profit = self.tax.profit_before_tax.total_value - self.tax.value

    def __str__(self):
        return ''
