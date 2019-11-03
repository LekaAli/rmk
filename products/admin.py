from django.contrib import admin
from products.models import Product, Sale, GrossProfit, Expense, ProfitBeforeTax, Tax, NetProfit


class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['average_revenue_per_month']


class ProductSeasonalityAdmin(admin.ModelAdmin):
    save_on_top = True


class SaleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'product', 'total_sale_revenue', 'period', 'created', 'modified')
    list_display_links = ('id', 'product')


class GrossProfitAdmin(admin.ModelAdmin):
    save_on_top = True


class ExpenseAdmin(admin.ModelAdmin):
    save_on_top = True


class ProfitBeforeTaxAdmin(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['gross', 'expense', 'total_gross_value']


class TaxAdmin(admin.ModelAdmin):
    save_on_top = True


class NetProfitAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(GrossProfit, GrossProfitAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ProfitBeforeTax, ProfitBeforeTaxAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(NetProfit, NetProfitAdmin)
