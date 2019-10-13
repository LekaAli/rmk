from django.contrib import admin
from dates.models import FinancialYear
# Register your models here.


class FinancialYearAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(FinancialYear, FinancialYearAdmin)
