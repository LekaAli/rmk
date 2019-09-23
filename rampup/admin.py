from django.contrib import admin
from rampup.models import ProductRampUp


class ProductRampUpAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(ProductRampUp, ProductRampUpAdmin)