from django.contrib import admin
from .models import Purchases


class Purchasesadmin(admin.ModelAdmin):
    list_display = ["purchaseinvoice", "purchasedate", "purchasegrandtotal", "mgr_id"]


admin.site.register(Purchases, Purchasesadmin)



