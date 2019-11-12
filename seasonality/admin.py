from django.contrib import admin
from seasonality.models import Seasonality, SeasonalityValue


class SeasonalityAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ['id', 'name', 'seasonality_type', 'year']
    list_display_links = ['id', 'name', 'seasonality_type', 'year']


class SeasonalityValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'seasonality', 'month', 'percentage']
    list_display_links = ['id', 'seasonality', 'month', 'percentage']


admin.site.register(Seasonality, SeasonalityAdmin)
admin.site.register(SeasonalityValue, SeasonalityValueAdmin)
