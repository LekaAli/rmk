from django.contrib import admin
from rampup.models import ProductRampUp


class ProductRampUpAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'product', 'financial_year', 'month', 'demand_value', 'demand_percentage']
    list_display_links = ['id', 'product', 'financial_year', 'month', 'demand_value', 'demand_percentage']
    readonly_fields = ['demand_percentage']


admin.site.register(ProductRampUp, ProductRampUpAdmin)