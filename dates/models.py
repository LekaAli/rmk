from django.db import models
from monthdelta import monthdelta
from django.urls import reverse
import datetime


class FinancialYear(models.Model):
    description = models.CharField(max_length=100, default='Year 1')
    start_date = models.DateField()
    end_date = models.DateField()
    inflation = models.FloatField(default=0.00, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Financial Year'
        verbose_name_plural = 'Financial Years'

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + datetime.timedelta(days=365)
        if self.end_date.year % 4 != 0 and self.end_date.year % 100 == 0 and self.end_date.year % 400 != 0:
            self.end_date = self.start_date + datetime.timedelta(days=364)
        super(FinancialYear, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.description


class Dates(models.Model):
        dates_video = models.ImageField(default='date.png',blank=True)
        number_of_years_projected = models.FloatField(default=10)
        year_end = models.DateField(blank=True, null=True)
        year_start = models.DateField(blank=True, null=True)
        previous_2_years_actuals_AFS = models.DateField(blank=True, null=True)
        interim_management_accounts = models.DateField(blank=True, null=True)
        Latest_signed_actuals_AFS = models.DateField(blank=True, null=True)
        start_projection_date=models.DateField(blank=True, null=True)
        month_1 = models.DateField(blank=True, null=True)
        month_2 = models.DateField(blank=True, null=True)
        month_3 = models.DateField(blank=True, null=True)
        month_4 = models.DateField(blank=True, null=True)
        month_5 = models.DateField(blank=True, null=True)
        month_6 = models.DateField(blank=True, null=True)
        month_7 = models.DateField(blank=True, null=True)
        month_8 = models.DateField(blank=True, null=True)
        month_9 = models.DateField(blank=True, null=True)
        month_10 = models.DateField(blank=True, null=True)
        month_11 = models.DateField(blank=True, null=True)
        month_12 = models.DateField(blank=True, null=True)
        month_13 = models.DateField(blank=True, null=True)
        month_14 = models.DateField(blank=True, null=True)
        month_15 = models.DateField(blank=True, null=True)
        month_16 = models.DateField(blank=True, null=True)
        month_17 = models.DateField(blank=True, null=True)
        month_18 = models.DateField(blank=True, null=True)
        month_19 = models.DateField(blank=True, null=True)
        month_20 = models.DateField(blank=True, null=True)
        month_21 = models.DateField(blank=True, null=True)
        month_22 = models.DateField(blank=True, null=True)
        month_23 = models.DateField(blank=True, null=True)
        month_24 = models.DateField(blank=True, null=True)
        month_25 = models.DateField(blank=True, null=True)
        month_26 = models.DateField(blank=True, null=True)
        month_27 = models.DateField(blank=True, null=True)
        month_28 = models.DateField(blank=True, null=True)
        month_29 = models.DateField(blank=True, null=True)
        month_30 = models.DateField(blank=True, null=True)
        month_31 = models.DateField(blank=True, null=True)
        month_32 = models.DateField(blank=True, null=True)
        month_33 = models.DateField(blank=True, null=True)
        month_34 = models.DateField(blank=True, null=True)
        month_35 = models.DateField(blank=True, null=True)
        month_36 = models.DateField(blank=True, null=True)
        year_1 = models.DateField(blank=True, null=True)
        year_2 = models.DateField(blank=True, null=True)
        year_3 = models.DateField(blank=True, null=True)
        year_4 = models.DateField(blank=True, null=True)
        year_5 = models.DateField(blank=True, null=True)
        year_6 = models.DateField(blank=True, null=True)
        year_7 = models.DateField(blank=True, null=True)
        year_8 = models.DateField(blank=True, null=True)
        year_9 = models.DateField(blank=True, null=True)
        year_10 = models.DateField(blank=True, null=True)

        @property
        def _get_month_1 (self, *args, **kwarg):
                return self.year_end + monthdelta(1)

        @property
        def _get_month_2 (self, *args, **kwarg):
                return self.year_end + monthdelta(2)

        @property
        def _get_month_3 (self, *args, **kwarg):
                return self.year_end + monthdelta(3)

        @property
        def _get_month_4 (self, *args, **kwarg):
                return self.year_end + monthdelta(4)

        @property
        def _get_month_5 (self, *args, **kwarg):
                return self.year_end + monthdelta(5)

        @property
        def _get_month_6 (self, *args, **kwarg):
                return self.year_end + monthdelta(6)

        @property
        def _get_month_7 (self, *args, **kwarg):
                return self.year_end + monthdelta(7)

        @property
        def _get_month_8 (self, *args, **kwarg):
                return self.year_end + monthdelta(8)

        @property
        def _get_month_9 (self, *args, **kwarg):
                return self.year_end + monthdelta(9)

        @property
        def _get_month_10 (self, *args, **kwarg):
                return self.year_end + monthdelta(10)

        @property
        def _get_month_11 (self, *args, **kwarg):
                return self.year_end + monthdelta(11)

        @property
        def _get_month_12 (self, *args, **kwarg):
                return self.year_end + monthdelta(12)

        @property
        def _get_year_1 (self, *args, **kwarg):
                return self.year_end + monthdelta(12)

        @property
        def _get_month_13 (self, *args, **kwarg):
                return self.year_end + monthdelta(13)

        @property
        def _get_month_14 (self, *args, **kwarg):
                return self.year_end + monthdelta(14)

        @property
        def _get_month_15 (self, *args, **kwarg):
                return self.year_end + monthdelta(15)

        @property
        def _get_month_16 (self, *args, **kwarg):
                return self.year_end + monthdelta(16)

        @property
        def _get_month_17 (self, *args, **kwarg):
                return self.year_end + monthdelta(17)

        @property
        def _get_month_18 (self, *args, **kwarg):
                return self.year_end + monthdelta(18)

        @property
        def _get_month_19 (self, *args, **kwarg):
                return self.year_end + monthdelta(19)

        @property
        def _get_month_20 (self, *args, **kwarg):
                return self.year_end + monthdelta(20)

        @property
        def _get_month_21 (self, *args, **kwarg):
                return self.year_end + monthdelta(21)

        @property
        def _get_month_22 (self, *args, **kwarg):
                return self.year_end + monthdelta(22)

        @property
        def _get_month_23 (self, *args, **kwarg):
                return self.year_end + monthdelta(23)


        @property
        def _get_month_24 (self, *args, **kwarg):
                return self.year_end + monthdelta(24)

        @property
        def _get_year_2 (self, *args, **kwarg):
                return self.year_end + monthdelta(24)

        @property
        def _get_month_25 (self, *args, **kwarg):
                return self.year_end + monthdelta(25)

        @property
        def _get_month_26 (self, *args, **kwarg):
                return self.year_end + monthdelta(26)

        @property
        def _get_month_27 (self, *args, **kwarg):
                return self.year_end + monthdelta(27)

        @property
        def _get_month_28 (self, *args, **kwarg):
                return self.year_end + monthdelta(28)

        @property
        def _get_month_29 (self, *args, **kwarg):
                return self.year_end + monthdelta(29)

        @property
        def _get_month_30 (self, *args, **kwarg):
                return self.year_end + monthdelta(30)

        @property
        def _get_month_31 (self, *args, **kwarg):
                return self.year_end + monthdelta(31)

        @property
        def _get_month_32 (self, *args, **kwarg):
                return self.year_end + monthdelta(32)

        @property
        def _get_month_33 (self, *args, **kwarg):
                return self.year_end + monthdelta(33)

        @property
        def _get_month_34 (self, *args, **kwarg):
                return self.year_end + monthdelta(34)

        @property
        def _get_month_35 (self, *args, **kwarg):
                return self.year_end + monthdelta(35)

        @property
        def _get_month_36 (self, *args, **kwarg):
                return self.year_end + monthdelta(36)

        @property
        def _get_year_3 (self, *args, **kwarg):
                return self.year_end + monthdelta(36)

        @property
        def _get_year_4 (self, *args, **kwarg):
                return self.year_end + monthdelta(48)

        @property
        def _get_year_5 (self, *args, **kwarg):
                return self.year_end + monthdelta(60)

        @property
        def _get_year_6 (self, *args, **kwarg):
                return self.year_end + monthdelta(72)

        @property
        def _get_year_7 (self, *args, **kwarg):
                return self.year_end + monthdelta(84)

        @property
        def _get_year_8 (self, *args, **kwarg):
                return self.year_end + monthdelta(96)

        @property
        def _get_year_9 (self, *args, **kwarg):
                return self.year_end + monthdelta(108)

        @property
        def _get_year_10 (self, *args, **kwarg):
                return self.year_end + monthdelta(120)

        def save(self, *args, **kwargs):
                self.month_1 = self._get_month_1
                self.month_2 = self._get_month_2
                self.month_3 = self._get_month_3
                self.month_4 = self._get_month_4
                self.month_5 = self._get_month_5
                self.month_6 = self._get_month_6
                self.month_7 = self._get_month_7
                self.month_8 = self._get_month_8
                self.month_9 = self._get_month_9
                self.month_10 = self._get_month_10
                self.month_11 = self._get_month_11
                self.month_12 = self._get_month_12
                self.month_13 = self._get_month_13
                self.month_14 = self._get_month_14
                self.month_15 = self._get_month_15
                self.month_16 = self._get_month_16
                self.month_17 = self._get_month_17
                self.month_18 = self._get_month_18
                self.month_19 = self._get_month_19
                self.month_20 = self._get_month_20
                self.month_21 = self._get_month_21
                self.month_22 = self._get_month_22
                self.month_23 = self._get_month_23
                self.month_24 = self._get_month_24
                self.month_25 = self._get_month_25
                self.month_26 = self._get_month_26
                self.month_27 = self._get_month_27
                self.month_28 = self._get_month_28
                self.month_29 = self._get_month_29
                self.month_30 = self._get_month_30
                self.month_31 = self._get_month_31
                self.month_32 = self._get_month_32
                self.month_33 = self._get_month_33
                self.month_34 = self._get_month_34
                self.month_35 = self._get_month_35
                self.month_36 = self._get_month_36
                self.year_1 = self._get_year_1
                self.year_2 = self._get_year_2
                self.year_3 = self._get_year_3
                self.year_4 = self._get_year_4
                self.year_5 = self._get_year_5
                self.year_6 = self._get_year_6
                self.year_7 = self._get_year_7
                self.year_8 = self._get_year_8
                self.year_9 = self._get_year_9
                self.year_10 = self._get_year_10

                super(Dates, self).save(*args, **kwargs)

        def get_absolute_url(self):
                return reverse('dates:CreateDates')
