from django.contrib import admin
from products.models import Product, Sale


class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['average_revenue_per_month']


class ProductSeasonalityAdmin(admin.ModelAdmin):
    save_on_top = True


class SaleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'product', 'total_sale_revenue', 'period', 'created', 'modified')
    list_display_links = ('id', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
