from django.contrib import admin
from inflation.models import Inflation


class InflationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'description', 'value', 'percentage', 'financial_year']
    list_display_links = ['id', 'description']
    readonly_fields = ['financial_year', 'percentage']


admin.site.register(Inflation, InflationAdmin)
