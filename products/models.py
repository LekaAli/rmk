from django.db import models
from django.urls import reverse
from dates.models import FinancialYear


class Product(models.Model):
    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    projection_start = models.PositiveSmallIntegerField(blank=False, null=True, choices=MONTHS)
    average_unit_price = models.FloatField(default=10)
    average_quantity_per_month = models.FloatField(default=1.00)
    average_revenue_per_month = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

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
    product = models.ForeignKey(Product, related_name='product_sale', on_delete=models.CASCADE, blank=True, null=True)
    total_sale_revenue = models.FloatField(default=0.00)
    period = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Sale'
        verbose_name_plural = 'Product Sales'

    def save(self, *args, **kwargs):
        super(Sale, self).save(*args, *kwargs)

    def __str__(self):
        return '%s: %.2f' % (self.product.name, self.total_sale_revenue)


class GrossProfit(models.Model):
    product = models.ForeignKey(Product, related_name='product_gross_profit', on_delete=models.CASCADE, blank=True, null=True)
    financial_year = models.ForeignKey(
        FinancialYear, related_name='gross_profit_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(default=1)
    cost_of_sale = models.FloatField(default=0.00)
    gross_profit_value = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gross Profit'
        verbose_name_plural = 'Gross Profits'

    def save(self, *args, **kwargs):
        from revenues.models import ProductRevenue
        product_revenue = ProductRevenue.objects.filter(product_id=self.product.id, financial_year_id=self.financial_year.id, month=self.month)
        if product_revenue.count() > 0:
            revenue = product_revenue.first()
            self.gross_profit_value = revenue.product_revenue - self.cost_of_sale
        else:
            self.gross_profit_value = 0
        super(GrossProfit, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s = %s' % (self.product.sale, self.cost_of_sale, self.gross_profit)


class Expense(models.Model):
    sale = models.ForeignKey(Sale, related_name='sale_expenses', on_delete=models.CASCADE, blank=True, null=True)
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
    total_gross_value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profit Before Tax'
        verbose_name_plural = 'Profit Before Taxes'

    def save(self, *args, **kwargs):
        super(ProfitBeforeTax, self).save(*args, **kwargs)
        self.total_gross_value = self.gross.gross_profit_value - self.expense

    def __str__(self):
        return 'Total Gross Value: %s' % self.total_gross_value


class Tax(models.Model):
    profit_before_tax = models.ForeignKey(ProfitBeforeTax, related_name='profit_before_tax', on_delete=models.CASCADE, blank=True, null=True)
    total_tax_value = models.FloatField(default=0.00)
    tax_percentage = models.FloatField(default=1.00)
    profit_loss_value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def save(self, *args, **kwargs):
        super(Tax, self).save(*args, **kwargs)
        if self.profit_before_tax.total_gross_value <= 0:
            self.total_tax_value = 0
        else:
            # calculate tax
            if self.profit_loss_value == 0:
                self.total_tax_value = self.profit_before_tax.total_gross_value(self.tax_percentage / float(100))
            else:
                # cover loss for previous years
                profit_after_loss_deduction = self.profit_before_tax.total_gross_value - self.profit_loss_value
                if profit_after_loss_deduction > 0:
                    self.profit_loss_value = 0
                    self.total_tax_value = profit_after_loss_deduction(self.tax_percentage / float(100))
                else:
                    self.profit_loss_value = abs(profit_after_loss_deduction)
                    self.total_tax_value = 0

    def __str__(self):
        return 'Total tax payable: %s' % self.total_tax_value


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
        self.net_profit = self.tax.profit_before_tax.total_value - self.tax.total_tax_value

    def __str__(self):
        return 'Net Profit: %s' % self.net_profit
