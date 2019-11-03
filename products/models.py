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
        product_revenue = ProductRevenue.objects.filter(financial_year_id=self.financial_year.id, month=self.month)
        if product_revenue.count() > 0:
            revenue = product_revenue.first()
            self.gross_profit_value = revenue.product_revenue - (self.cost_of_sale / float(100) * revenue.product_revenue)
        else:
            self.gross_profit_value = 0
        super(GrossProfit, self).save(*args, **kwargs)

    def __str__(self):
        return '%s - %s = %s' % (self.product.sale, self.cost_of_sale, self.gross_profit)


class Expense(models.Model):
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
    financial_year = models.ForeignKey(FinancialYear, related_name='expense_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(choices=MONTHS)
    is_fixed = models.BooleanField()
    value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def save(self, *args, **kwargs):
        super(Expense, self).save(*args, **kwargs)

    def __str__(self):
        return '%s percent of expenses' % self.value if self.is_fixed is True else '%s for expenses' % self.value


class ProfitBeforeTax(models.Model):
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
    financial_year = models.ForeignKey(FinancialYear, related_name='profit_before_tax_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True)
    gross = models.FloatField(default=0.00)
    expense = models.FloatField(default=0.00)
    monthly_gross_value = models.FloatField(default=0.00)
    total_gross_value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profit Before Tax'
        verbose_name_plural = 'Profit Before Taxes'

    def save(self, *args, **kwargs):
        gross_values = GrossProfit.objects.filter(financial_year=self.financial_year.id, month=self.month)
        if gross_values.count() > 0:
            gross_value = sum([gross.gross_profit_value for gross in gross_values])
            expenses = Expense.objects.filter(month=self.month)

            fixed_expenses = sum([expense.value if expenses.financial_year == self.financial_year else expense.value + (self.financial_year.inflation / float(100) * expense.value) for expense in expenses if expense.is_fixed is True])
            not_fixed_expenses = sum([(expense.value / float(100) * gross_value) for expense in expenses if expense.is_fixed is False])

            self.monthly_gross_value = gross_value - (fixed_expenses + not_fixed_expenses)
            self.total_gross_value = self.total_gross_value + self.monthly_gross_value
        else:
            self.monthly_gross_value = 0
        super(ProfitBeforeTax, self).save(*args, **kwargs)

    def __str__(self):
        return 'Total Gross Value: %s' % self.total_gross_value


class Tax(models.Model):
    financial_year = models.ForeignKey(FinancialYear, related_name='tax_f_year', on_delete=models.CASCADE, blank=False, null=True)
    tax_percentage = models.FloatField(default=1.00)
    profit_loss_value = models.FloatField(default=0.00)
    total_tax_value = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def save(self, *args, **kwargs):
        profit_before_tax = ProfitBeforeTax.objects.filter(financial_year=self.financial_year.id)
        if profit_before_tax.count() > 0:
            total_gross_value = sum([p_before_tax.total_gross_value for p_before_tax in profit_before_tax])
        else:
            total_gross_value = 0.00

        if total_gross_value <= 0:
            self.total_tax_value = 0
            self.profit_loss_value = abs(total_gross_value)
        else:
            # calculate tax
            previous_taxes = Tax.objects.all()
            if previous_taxes.count() > 0:
                previous_tax = previous_taxes.lastest()
                if previous_tax.profit_loss_value == 0:
                    self.total_tax_value = total_gross_value * self.tax_percentage / float(100)
                else:
                    # cover loss for previous years
                    profit_after_loss_deduction = total_gross_value - previous_tax.profit_loss_value
                    if profit_after_loss_deduction > 0:
                        self.profit_loss_value = 0
                        self.total_tax_value = profit_after_loss_deduction * self.tax_percentage / float(100)
                    else:
                        self.profit_loss_value = abs(profit_after_loss_deduction)
                        self.total_tax_value = 0
            self.total_tax_value = total_gross_value * self.tax_percentage / float(100)
        super(Tax, self).save(*args, **kwargs)

    def __str__(self):
        return 'Total tax payable: %s' % self.total_tax_value


class NetProfit(models.Model):
    financial_year = models.ForeignKey(FinancialYear, related_name='net_profit_f_year', on_delete=models.CASCADE, blank=False, null=True)
    net_profit = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Net Profit'
        verbose_name_plural = 'Net Profits'

    def save(self, *args, **kwargs):
        taxes = Tax.objects.filter(financial_year=self.financial_year.id)
        profits_before_tax = ProfitBeforeTax.objects.filter(financial_year=self.financial_year.id)
        if profits_before_tax.count() > 0:
            profit_before_tax_value = sum([p_before_tax.total_gross_value for p_before_tax in profits_before_tax])
            if taxes.count() > 0:
                self.net_profit = profit_before_tax_value - taxes.first().total_tax_value
        else:
            profit_before_tax_value = 0
            self.net_profit = profit_before_tax_value

        super(NetProfit, self).save(*args, **kwargs)

    def __str__(self):
        return 'Net Profit: %s' % self.net_profit
