from django.db import models
from products.models import Sale
from dates.models import FinancialYear
from rampup.models import RampUp
from seasonality.models import Seasonality


class Revenue(models.Model):
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
    product = models.ForeignKey('products.Product', related_name='revenue_product', on_delete=models.CASCADE, null=True,
                                blank=True)
    financial_year = models.ForeignKey(FinancialYear, related_name='revenue_f_year', on_delete=models.CASCADE,
                                       blank=False, null=True)
    month = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True)
    inflation = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    product_revenue = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Revenue'
        verbose_name_plural = 'Products Revenue'

    def calculate_product_revenue(self, product_projection):
        rampup_percentage = 1.0
        seasonality_percentage = 1.0
        for monthly_value in product_projection.seasonality.seasonality_values.all():
            if monthly_value.month != self.month:
                continue
            seasonality_percentage = monthly_value.month_percentage
            break
        for monthly_value in product_projection.rampup.rampup_values.all():
            if monthly_value.month != self.month:
                continue
            rampup_percentage = monthly_value.month_percentage
            break
        if product_projection.seasonality.year == self.financial_year:
            product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                              rampup_percentage
        else:
            if product_projection.rampup.will_roll_over is True:
                if product_projection.seasonality.will_roll_over is True:
                    product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                                      rampup_percentage * \
                                      (1 + self.financial_year.inflation_value)
                else:
                    seasonality_month = Seasonality.objects.filter(year=self.financial_year, seasonality_values__month=self.month).first()
                    seasonality_percentage = seasonality_month.month_percentage
                    product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                                      rampup_percentage * \
                                      (1 + self.financial_year.inflation_value)
            else:
                rampup_month = RampUp.objects.filter(year=self.financial_year,
                                                     rampup_values__month=self.month)
                if rampup_month.count() > 0:
                    rampup_percentage = rampup_month.first().month_percentage
                    if product_projection.seasonality.will_roll_over is False:
                        seasonality_month = Seasonality.objects.filter(year=self.financial_year,
                                                                       seasonality_values__month=self.month)
                        if seasonality_month.count() > 0:
                            seasonality_percentage = seasonality_month.first().month_percentage
                        else:
                            seasonality_percentage = 1.0
                else:
                    rampup_percentage = 1.0
                product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                                      rampup_percentage * (1 + self.financial_year.inflation_value)

        return product_revenue
    
    def monthly_revenue_count(self):
        
        past_monthly_revenue_count = len(Revenue.objects.filter(product=self.product).values_list('financial_year', flat=True))
        if past_monthly_revenue_count <= 12:
            return 1
        elif 12 < past_monthly_revenue_count <= 24:
            return 2
        else:
            year_value = past_monthly_revenue_count - 24
            return 3 if abs(year_value - 2) == 0 else self.calc_year_value(year_value)
    
    @staticmethod
    def calc_year_value(value):
        
        return 4 + abs(value - 2)
    
    def save(self, *args, **kwargs):
        
        product_estimations = self.product.product_link.all()
        self.inflation = self.financial_year.inflation
        revenue_years_count = self.monthly_revenue_count()
        past_years_count = Sale.objects.filter(product=self.product).values_list('period', flat=True).distinct().count()
        if product_estimations.count() == 1:  # Kgonagalo ya gore ngwaga o šomišwe go feta gatee.
            product_projection_instance = self.product.product_link.first()
            if revenue_years_count in [1, 2]:
                self.product_revenue = self.calculate_product_revenue(product_projection_instance)
            elif revenue_years_count == 3:
                monthly_product_revenue = sum(Sale.objects.filter(period=2).values_list('month_sale', flat=True))
                self.product_revenue = (self.financial_year.inflation_value + 1) * float(monthly_product_revenue)
            else:
                past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_years_count)
                self.product_revenue = float(past_year_revenue.first().total_sale_revenue) * (1 + self.financial_year.inflation_value)
            
        elif product_estimations.count() == 2:  # mengwaga e mebedi
            product_projection_instances = self.product.product_link.all()
            projection_instance = [instance for instance in product_projection_instances if instance.rampup.year == self.financial_year]
            
            if revenue_years_count in [1, 2]:
                self.product_revenue = self.calculate_product_revenue(projection_instance)
            elif revenue_years_count == 3:
                monthly_product_revenue = sum(Sale.objects.filter(period=2).values_list('month_sale', flat=True))
                self.product_revenue = (self.financial_year.inflation_value + 1) * monthly_product_revenue
            else:
                past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_years_count)
                self.product_revenue = float(past_year_revenue.first().total_sale_revenue) * (1 + self.financial_year.inflation_value)
               
        else:  # tša go feta mengwaga ye mebedi
            self.product_revenue = 0
           
        if revenue_years_count < 3:
            product_sale = Sale.objects.filter(product_id=self.product.id, period=revenue_years_count)
            if product_sale.count() == 0:
                product_sale = Sale(product_id=self.product.id, period=revenue_years_count)
                if self.month:
                    product_sale.month = self.month
                product_sale.month_sale = self.product_revenue
                product_sale.save()
            else:
                product_sale = product_sale.last()
                if not self.pk:
                    product_sale.month_sale = float(product_sale.month_sale) + self.product_revenue
                    product_sale.save()
        else:
            if not self.pk:
                product_sale = Sale(product_id=self.product.id, period=past_years_count + 1)
                if self.month:
                    product_sale.month = self.month
                product_sale.total_sale_revenue = self.product_revenue
                product_sale.save()
        super(Revenue, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.product.name, self.product_revenue)
