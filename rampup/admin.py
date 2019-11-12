from django.contrib import admin
from rampup.models import RampUp, RampUpValue


class RampUpAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'rampup_type', 'year']
    list_display_links = ['id', 'name', 'rampup_type', 'year']


class RampUpValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['id', 'rampup', 'month', 'percentage']
    list_display_links = ['id', 'rampup', 'month', 'percentage']


admin.site.register(RampUp, RampUpAdmin)
admin.site.register(RampUpValue, RampUpValueAdmin)