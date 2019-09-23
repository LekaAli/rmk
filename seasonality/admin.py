from django.contrib import admin
from seasonality.models import ProductSeasonality


class ProductSeasonalityAdmin(admin.ModelAdmin):

    save_on_top = True
    readonly_fields = ['month', 'demand_percentage']
    list_display = ['id', 'name', 'demand_value', 'demand_percentage', 'product', 'month']
    list_display_links = ['id', 'name']


admin.site.register(ProductSeasonality, ProductSeasonalityAdmin)
