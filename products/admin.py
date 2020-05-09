from django.contrib import admin
from products.models import Product, Sale, GrossProfit, Expense, ProfitBeforeTax, Tax, NetProfit, CostOfSale
from products.models import TaxValue, DefaultValue


class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'average_unit_price', 'average_quantity_per_month', 'average_revenue_per_month', 'projection_start']
    list_display_links = ['id', 'name', 'average_unit_price', 'average_quantity_per_month', 'average_revenue_per_month', 'projection_start']
    readonly_fields = ['average_revenue_per_month']


class ProductSeasonalityAdmin(admin.ModelAdmin):
    save_on_top = True


class SaleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'product', 'period', 'month', 'month_sale', 'total_sale_revenue', 'created', 'modified')
    list_display_links = ('id', 'product', 'period', 'month', 'month_sale', 'total_sale_revenue', 'created', 'modified')
    # readonly_fields = ['product', 'month', 'month_sale', 'period', 'total_sale_revenue']


class GrossProfitAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'product', 'financial_year', 'month', 'cost_of_sale', 'cost_of_sale_value', 'gross_profit_value']
    list_display_links = ['product', 'financial_year', 'month',  'cost_of_sale', 'cost_of_sale_value']
    readonly_fields = ['cost_of_sale_value', 'gross_profit_value']


class ExpenseAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'description', 'is_fixed', 'value']
    list_display_links = ['id', 'description', 'is_fixed', 'value']


class ProfitBeforeTaxAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'financial_year', 'month', 'expense', 'profit_before_tax']
    list_display_links = ['id', 'financial_year', 'month', 'expense', 'profit_before_tax']
    readonly_fields = ['expense', 'profit_before_tax']


class TaxAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'financial_year', 'month', 'tax_percentage', 'profit_loss_value', 'total_tax_value']
    list_display_links = ['id', 'financial_year', 'month', 'tax_percentage', 'profit_loss_value', 'total_tax_value']
    readonly_fields = ['profit_loss_value', 'total_tax_value']


class NetProfitAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'financial_year', 'month', 'net_profit']
    list_display_links = ['id', 'financial_year', 'month', 'net_profit']
    

class CostOfSaleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'percentage', 'created', 'modified']
    list_display_links = ['id', 'percentage', 'created', 'modified']


class ProductSeasonalityRampUpAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'product', 'seasonality', 'rampup']
    list_display_links = ['id', 'product', 'seasonality', 'rampup']


class TaxValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'financial_year', 'value']
    list_display_links = ['id', 'financial_year', 'value']
    

class DefaultValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'app_name', 'period', 'value']
    list_display_links = ['id', 'app_name', 'period', 'value']
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(GrossProfit, GrossProfitAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ProfitBeforeTax, ProfitBeforeTaxAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(NetProfit, NetProfitAdmin)
admin.site.register(CostOfSale, CostOfSaleAdmin)
admin.site.register(TaxValue, TaxValueAdmin)
admin.site.register(DefaultValue, DefaultValueAdmin)
