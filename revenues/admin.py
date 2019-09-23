from django.contrib import admin
from revenues.models import ProductRevenue


class RevenueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'product', 'product_seasonality', 'product_revenue']
    list_display_links = ['id', 'product', 'product_seasonality']
    readonly_fields = ['product_revenue', 'inflation']


admin.site.register(ProductRevenue, RevenueAdmin)
