from django.db import models
from django.urls import reverse
from dates.models import FinancialYear
from rampup.models import RampUp


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
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    projection_start = models.PositiveSmallIntegerField(blank=False, null=True, choices=MONTHS)
    average_unit_price = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    average_quantity_per_month = models.PositiveIntegerField(default=1)
    average_revenue_per_month = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
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
    month = models.PositiveSmallIntegerField(blank=True, null=True)
    month_sale = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    total_sale_revenue = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    period = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Sale'
        verbose_name_plural = 'Product Sales'

    def save(self, *args, **kwargs):
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %.2f' % (self.product.name, self.total_sale_revenue)


class CostOfSale(models.Model):
    product = models.OneToOneField(Product, related_name='product_cost_of_sale', on_delete=models.CASCADE, blank=True, null=True, unique=True)
    percentage = models.FloatField(default=0, help_text="Cost of sale value should be a percentage")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cost Of Sale'
        verbose_name_plural = 'Cost Of Sales'

    def __str__(self):
        return '%s - %s' % (self.product.name, self.percentage)
    
    @property
    def _percentage(self):
        return self.percentage / 100
    
    def save(self, *args, **kwargs):
        self.percentage = self._percentage
        super(CostOfSale, self).save(*args, **kwargs)
       

class GrossProfit(models.Model):
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
    product = models.ForeignKey(
        Product, related_name='product_gross_profit', on_delete=models.CASCADE, blank=True, null=True)
    financial_year = models.ForeignKey(
        FinancialYear, related_name='gross_profit_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveSmallIntegerField(
        choices=MONTHS,
        blank=True,
        null=True, help_text="Month value from when a product projection begun until the end of the financial year")
    cost_of_sale = models.ForeignKey(
        CostOfSale, related_name='gross_cost_of_sale', on_delete=models.CASCADE, blank=True, null=True)
    cost_of_sale_value = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    gross_profit_value = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gross Profit'
        verbose_name_plural = 'Gross Profits'

    def save(self, *args, **kwargs):
        from revenues.models import Revenue
        product_revenue_listing = Revenue.objects.filter(
            financial_year_id=self.financial_year.id,
            product_id=self.product.id
        )
        if product_revenue_listing.count() > 1:
            product_revenue_instance = product_revenue_listing.filter(month=self.month).first()
        if product_revenue_listing.count() == 1:
            product_revenue_instance = product_revenue_listing.first()
            
        if product_revenue_listing.count() >= 1:
            self.cost_of_sale = self.product.product_cost_of_sale
            self.cost_of_sale_value = self.cost_of_sale.percentage * float(product_revenue_instance.product_revenue)
            self.gross_profit_value = float(product_revenue_instance.product_revenue) - self.cost_of_sale_value
        else:
            self.gross_profit_value = 0
        super(GrossProfit, self).save(*args, **kwargs)

    def __str__(self):
        return 'Product: %s; Year: %s; Month: %s; Gross Profit: %s' % (
            self.product.name,
            self.financial_year,
            self.month,
            self.gross_profit_value
        )


class Expense(models.Model):
    EXPENSE_TYPE = [(0, 'Operating'), (1, 'Administration'), (2, 'Payroll'), (3, 'Marketing')]
    description = models.CharField(max_length=120, blank=True, null=True)
    expense_type = models.PositiveSmallIntegerField(choices=EXPENSE_TYPE, blank=True, null=True)
    is_fixed = models.BooleanField()
    value = models.DecimalField(decimal_places=2, max_digits=15)
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
    expense = models.TextField(blank=True, null=True)
    profit_before_tax = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profit Before Tax'
        verbose_name_plural = 'Profit Before Taxes'
    
    @staticmethod
    def expense_in_categories(expense_category_dict, expense_instance, val):
        category_dict = dict(expense_instance.EXPENSE_TYPE)
        expense_category = category_dict.get(expense_instance.expense_type)
        if expense_category in expense_category_dict.keys():
            expense_category_dict.get(expense_category).update(
                {
                    expense_instance.description: val
                }
            )
        else:
            expense_category_dict[expense_category] = {
                expense_instance.description: val
            }
        return expense_category_dict
    
    def calculate_net_profit_before_tax(self, revenue_values):
        revenue_value = sum(revenue_values.values_list('product_revenue', flat=True))
        expenses = Expense.objects.all()
        expense_dict = dict()
        expense_category_dict = dict()
        if revenue_value > 0:
            inflation = self.financial_year.inflation / float(100)
            fixed_expenses = 0.0
            not_fixed_expenses = 0.0
            for expense in expenses:
                if expense.is_fixed is True:
                    expense_val = float(expense.value) + (inflation * float(expense.value))
                    fixed_expenses = fixed_expenses + expense_val
                    expense_dict.update(
                        {
                            expense.description: expense_val
                        }
                    )
                    self.expense_in_categories(expense_category_dict, expense, expense_val)
                    continue
                expense_val = (float(expense.value) / float(100) * float(revenue_value))
                not_fixed_expenses = not_fixed_expenses + expense_val
                expense_dict.update(
                    {
                        expense.description: expense_val
                    }
                )
                self.expense_in_categories(expense_category_dict, expense, expense_val)
            expense_dict['expense_total'] = fixed_expenses + not_fixed_expenses
            self.expense = expense_category_dict
            gross_profit_values = GrossProfit.objects.filter(
                financial_year=self.financial_year.id,
                month=self.month).values_list(
                'gross_profit_value', flat=True
            )
            gross_profit_monthly_total = sum(gross_profit_values)
            self.profit_before_tax = float(gross_profit_monthly_total) - float(expense_dict['expense_total'])
        else:
            self.profit_before_tax = 0.0
            for expense in expenses:
                expense_val = 0.0
                if expense.is_fixed is True:
                    expense_dict.update(
                        {
                            expense.description: expense_val
                        }
                    )
                    self.expense_in_categories(expense_category_dict, expense, expense_val)
                    continue
                expense_dict.update(
                    {
                        expense.description: expense_val
                    }
                )
                self.expense_in_categories(expense_category_dict, expense, expense_val)
            expense_dict['expense_total'] = 0.0
            # self.expense = expense_dict
            self.expense = expense_category_dict
       
    def save(self, *args, **kwargs):
    
        from revenues.models import Revenue
        if self.pk is None:
            revenue_values = Revenue.objects.filter(financial_year=self.financial_year.id, month=self.month)
            if revenue_values.count() > 0:  # monthly gross values
                self.calculate_net_profit_before_tax(revenue_values)
            else:
                revenue_values = Revenue.objects.filter(financial_year=self.financial_year.id)
                if revenue_values.count() > 0:  # yearly gross values
                    self.calculate_net_profit_before_tax(revenue_values)
                else:
                    self.monthly_gross_value = 0
        super(ProfitBeforeTax, self).save(*args, **kwargs)

    def __str__(self):
        return 'Total Profit Before Tax: %s' % self.profit_before_tax


class TaxValue(models.Model):
    financial_year = models.ForeignKey(FinancialYear, related_name='tax_value_f_year', on_delete=models.CASCADE, blank=False, null=True)
    value = models.FloatField(default=28.00)
    
    class Meta:
        verbose_name = 'Tax Value'
        verbose_name_plural = 'Tax Values'
        
    def __str__(self):
        return '%s' % self.value
    
    
class Tax(models.Model):
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
    financial_year = models.ForeignKey(FinancialYear, related_name='tax_f_year', on_delete=models.CASCADE, blank=False, null=True)
    month = models.PositiveIntegerField(choices=MONTHS, blank=True, null=True)
    tax_percentage = models.ForeignKey(TaxValue, on_delete=models.CASCADE, blank=True, related_name='tax_percent_value',null=True)
    profit_loss_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    total_tax_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def save(self, *args, **kwargs):
        profit_before_tax = ProfitBeforeTax.objects.filter(financial_year=self.financial_year.id, month=self.month)
        if profit_before_tax.count() > 0:
            total_profit_before_tax_value = sum([p_before_tax.profit_before_tax for p_before_tax in profit_before_tax])
        else:
            total_profit_before_tax_value = 0.00

        if total_profit_before_tax_value <= 0:
            self.total_tax_value = 0
            latest_tax_instance = Tax.objects.all().last()
            if latest_tax_instance:
                self.profit_loss_value = float(latest_tax_instance.profit_loss_value) + abs(total_profit_before_tax_value)
            else:
                self.profit_loss_value = abs(total_profit_before_tax_value)
        else:
            # calculate tax
            previous_taxes = Tax.objects.all()
            if previous_taxes.count() > 0:
                previous_tax = previous_taxes.last()
                if previous_tax.profit_loss_value == 0:
                    self.total_tax_value = total_profit_before_tax_value * float(self.tax_percentage.value) / float(100)
                else:
                    # cover loss for previous years
                    profit_after_loss_deduction = float(previous_tax.profit_loss_value) - total_profit_before_tax_value
                    if profit_after_loss_deduction >= 0:
                        self.profit_loss_value = profit_after_loss_deduction
                        self.total_tax_value = 0  # profit_after_loss_deduction * float(self.tax_percentage.value) / float(100)
                    else:
                        self.profit_loss_value = 0  # abs(profit_after_loss_deduction)
                        self.total_tax_value = abs(profit_after_loss_deduction) * float(self.tax_percentage.value) / float(100)  # 0
            else:
                self.total_tax_value = total_profit_before_tax_value * float(self.tax_percentage.value) / float(100)
        super(Tax, self).save(*args, **kwargs)

    def __str__(self):
        return 'Total tax payable: %s' % self.total_tax_value


class NetProfit(models.Model):
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
    financial_year = models.ForeignKey(
        FinancialYear,
        related_name='net_profit_f_year',
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    month = models.PositiveIntegerField(choices=MONTHS, blank=True, null=True)
    net_profit = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Net Profit'
        verbose_name_plural = 'Net Profits'

    def save(self, *args, **kwargs):
        taxes = Tax.objects.filter(financial_year=self.financial_year.id, month=self.month)
        profits_before_tax = ProfitBeforeTax.objects.filter(financial_year=self.financial_year.id, month=self.month)
        if profits_before_tax.count() > 0:
            profit_before_tax_value = sum([p_before_tax.profit_before_tax for p_before_tax in profits_before_tax])
            if taxes.count() > 0:
                self.net_profit = profit_before_tax_value - float(taxes.first().total_tax_value)
        else:
            profit_before_tax_value = 0
            self.net_profit = profit_before_tax_value

        super(NetProfit, self).save(*args, **kwargs)

    def __str__(self):
        return 'Net Profit: %s' % self.net_profit
    
    
class DefaultValue(models.Model):
    
    RAMPUP = 0
    SEASONALITY = 1
    INFLATION = 2
    TAX = 3
    APP_CHOICES = (
        (RAMPUP, 'RAMP UP'),
        (SEASONALITY, 'SEASONALITY'),
        (INFLATION, 'INFLATION'),
        (TAX, 'TAX'),
    )
    PERIOD_CHOICES = (
        (1, 'MONTH'),
        (2, 'YEAR')
    )
    app_name = models.PositiveSmallIntegerField(choices=APP_CHOICES)
    period = models.PositiveSmallIntegerField(choices=PERIOD_CHOICES)
    value = models.FloatField()
    
    class Meta:
        verbose_name = 'Default Value'
        verbose_name_plural = 'Default Values'
        
    def save(self, *args, **kwargs):
        super(DefaultValue, self).save(*args, **kwargs)

