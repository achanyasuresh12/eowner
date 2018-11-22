from django.contrib import admin
from .models import Itemstock


class ItemstockAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "purchasedate", "renewaldate", "price"]


admin.site.register(Itemstock, ItemstockAdmin)
