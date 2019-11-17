from django.db import models
from products.models import Sale
from dates.models import FinancialYear
# from seasonality.models import ProductSeasonality
# from rampup.models import ProductRampUp


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
        product_revenue = 0.0
        if product_projection.seasonality.year == self.financial_year:
            product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                              rampup_percentage
        else:
            if product_projection.seasonality.will_roll_over is True:
                product_revenue = float(self.product.average_revenue_per_month) * seasonality_percentage * \
                                  rampup_percentage * \
                                  (1 + self.financial_year.inflation_value)
            else:
                pass
        return product_revenue
    
    def monthly_revenue_count(self):
        
        revenue_count = Revenue.objects.all().values_list('financial_year', flat=True)
        current_year = Revenue.objects.filter(financial_year=self.financial_year)
        past_monthly_revenue_count = revenue_count.count() + 1 if current_year.count() == 0 else revenue_count.count()
        if past_monthly_revenue_count <= 12:
            return 1
        elif 12 < past_monthly_revenue_count <= 24:
            return 2
        elif past_monthly_revenue_count == 25:
            return 3
        else:
            return 4
    
    def save(self, *args, **kwargs):
        
        product_estimations = self.product.product_link.all()
        self.inflation = self.financial_year.inflation
        revenue_years_count = self.monthly_revenue_count()
        if product_estimations.count() == 1:  # Kgonagalo ya gore ngwaga o šomišwe go feta gatee.
            product_projection_instance = self.product.product_link.first()
            if revenue_years_count in [1, 2]:
                self.product_revenue = self.calculate_product_revenue(product_projection_instance)
            elif revenue_years_count == 3:
                monthly_product_revenue = sum(Sale.objects.filter(period=2).values_list('month_sale', flat=True))
                self.product_revenue = (self.financial_year.inflation_value + 1) * monthly_product_revenue
            else:
                past_years_count = Sale.objects.all().values_list('period', flat=True).distinct().count()
                past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_years_count - 1)
                self.product_revenue = past_year_revenue.first().total_sale_revenue * (1 + self.financial_year.inflation_value)
            
        elif product_estimations.count() == 2:  # mengwaga e mebedi
            product_projection_instances = self.product.product_link.all()
            projection_instance = [instance for instance in product_projection_instances if instance.rampup.year == self.financial_year]
            
            if revenue_years_count in [1, 2]:
                self.product_revenue = self.calculate_product_revenue(projection_instance)
            elif revenue_years_count == 3:
                monthly_product_revenue = sum(Sale.objects.filter(period=2).values_list('month_sale', flat=True))
                self.product_revenue = (self.financial_year.inflation_value + 1) * monthly_product_revenue
            else:
                past_years_count = Sale.objects.all().values_list('period', flat=True).distinct().count()
                past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_years_count - 1)
                self.product_revenue = past_year_revenue.first().total_sale_revenue * (1 + self.financial_year.inflation_value)
               
        else:  # tša go feta mengwaga ye mebedi
            self.product_revenue = 0
           
        if revenue_years_count < 3:
            product_sale = Sale.objects.filter(product_id=self.product.id, period=revenue_years_count, month=self.month)
            if len(product_sale) == 0:
                product_sale = Sale(product_id=self.product.id, period=revenue_years_count, month=self.month)
                product_sale.month_sale = self.product_revenue
                product_sale.save()
            else:
                product_sale = product_sale.first()
                if not self.pk:
                    product_sale.month_sale = product_sale.month_sale + self.product_revenue
                    product_sale.save()
        else:
            product_sale = Sale.objects.filter(product_id=self.product.id, period=revenue_years_count)
            if len(product_sale) == 0:
                product_sale = Sale(product_id=self.product.id, period=revenue_years_count)
                product_sale.total_sale_revenue = self.product_revenue
                product_sale.save()
            else:
                product_sale = product_sale.first()
                if not self.pk:
                    product_sale.total_sale_revenue = product_sale.total_sale_revenue + self.product_revenue
                    product_sale.save()
        super(Revenue, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.product.name, self.product_revenue)

# class ProductRevenue(models.Model):
#     MONTHS = (
#         (1, 'January'),
#         (2, 'February'),
#         (3, 'March'),
#         (4, 'April'),
#         (5, 'May'),
#         (6, 'June'),
#         (7, 'July'),
#         (8, 'August'),
#         (9, 'September'),
#         (10, 'October'),
#         (11, 'November'),
#         (12, 'December'),
#     )
#     product = models.ForeignKey('products.Product', related_name='revenue_product', on_delete=models.CASCADE, null=True, blank=True)
#     financial_year = models.ForeignKey(FinancialYear, related_name='revenue_f_year', on_delete=models.CASCADE, blank=False, null=True)
#     month = models.PositiveSmallIntegerField(choices=MONTHS, blank=True, null=True)
#     inflation = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
#     product_revenue = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
#     created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     modified = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Product Revenue'
#         verbose_name_plural = 'Products Revenue'
#
#     def save(self, *args, **kwargs):
#
#         product_years = ProductSeasonality.objects.filter(
#             product_id=self.product.id
#         ).values_list(
#             'financial_year',
#             flat=True
#         ).distinct()
#         year_count = product_years.count()
#         product_seasonality = ProductSeasonality.objects.filter(
#             product_id=self.product.id,
#             month=self.month,
#             financial_year=self.financial_year.id
#         ).first()
#         product_rampup = ProductRampUp.objects.filter(
#             product_id=self.product.id,
#             month=self.month,
#             financial_year=self.financial_year.id
#         ).first()
#         self.inflation = product_seasonality.financial_year.inflation
#         self.financial_year = product_seasonality.financial_year
#         self.month = product_seasonality.month
#         if len(product_years) in [0, 1]:
#             self.product_revenue = self.product.average_revenue_per_month * product_seasonality.demand_percentage * product_rampup.demand_percentage
#         elif len(product_years) == 2:
#             self.product_revenue = self.product.average_revenue_per_month * (
#                     1 + self.inflation) * product_seasonality.demand_percentage
#         elif len(product_years) == 3:
#             self.product_revenue = self.product.average_revenue_per_month * (1 + self.inflation) * 12
#         else:
#             past_year = year_count - 1
#             past_year_revenue = Sale.objects.filter(product_id=self.product.id, period=past_year)
#             self.product_revenue = past_year_revenue.first().total_sale_revenue * (1 + self.inflation)
#         if len(product_years) < 3:
#             product_sale = Sale.objects.filter(product_id=self.product.id, period=year_count, month=self.month)
#             if len(product_sale) == 0:
#                 product_sale = Sale(product_id=self.product.id, period=year_count, month=self.month)
#                 product_sale.month_sale = self.product_revenue
#                 product_sale.save()
#             else:
#                 product_sale = product_sale.first()
#                 if not self.pk:
#                     product_sale.month_sale = product_sale.month_sale + self.product_revenue
#                     product_sale.save()
#         else:
#             product_sale = Sale.objects.filter(product_id=self.product.id, period=year_count)
#             if len(product_sale) == 0:
#                 product_sale = Sale(product_id=self.product.id, period=year_count)
#                 product_sale.total_sale_revenue = self.product_revenue
#                 product_sale.save()
#             else:
#                 product_sale = product_sale.first()
#                 if not self.pk:
#                     product_sale.total_sale_revenue = product_sale.total_sale_revenue + self.product_revenue
#                     product_sale.save()
#         super(ProductRevenue, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return '%s' % self.product_revenue
