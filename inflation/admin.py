from django.contrib import admin
from inflation.models import Inflation


class InflationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'description', 'value', 'percentage', 'year']
    list_display_links = ['id', 'description']
    readonly_fields = ['year', 'percentage']


admin.site.register(Inflation, InflationAdmin)
