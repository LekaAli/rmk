from django.contrib import admin
from seasonality.models import Seasonality, SeasonalityValue


class SeasonalityAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ['id', 'name', 'seasonality_type', 'year']
    list_display_links = ['id', 'name', 'seasonality_type', 'year']
    filter_horizontal = ['seasonality_values']


class SeasonalityValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'month', 'percentage']
    list_display_links = ['id', 'month', 'percentage']


admin.site.register(Seasonality, SeasonalityAdmin)
admin.site.register(SeasonalityValue, SeasonalityValueAdmin)
