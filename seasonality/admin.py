from django.contrib import admin
from seasonality.models import ProductSeasonality


class ProductSeasonalityAdmin(admin.ModelAdmin):

    save_on_top = True
    readonly_fields = ['demand_percentage']
    list_display = ['id', 'demand_value', 'demand_percentage', 'product', 'month']
    list_display_links = ['id', 'demand_value', 'demand_percentage', 'product', 'month']


admin.site.register(ProductSeasonality, ProductSeasonalityAdmin)
