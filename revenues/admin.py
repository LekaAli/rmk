from django.contrib import admin
from revenues.models import ProductRevenue


class RevenueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'product', 'financial_year', 'month', 'product_revenue']
    list_display_links = ['id', 'product', 'financial_year']
    readonly_fields = ['product_revenue', 'inflation']


admin.site.register(ProductRevenue, RevenueAdmin)
