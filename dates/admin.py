from django.contrib import admin
from dates.models import FinancialYear
# Register your models here.


class FinancialYearAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'start_date', 'end_date', 'inflation']
    list_display_links = ['id', 'start_date', 'end_date', 'inflation']
    readonly_fields = ['end_date']


admin.site.register(FinancialYear, FinancialYearAdmin)
