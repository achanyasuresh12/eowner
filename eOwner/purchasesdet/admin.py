from django.contrib import admin
from .models import Purchasesdetails


class Purchasesdetailsadmin(admin.ModelAdmin):
    list_display = ["itemname", "itemquantity", "itembasicrate", "itemunittotal", "purchaseinvoice"]


admin.site.register(Purchasesdetails, Purchasesdetailsadmin)

