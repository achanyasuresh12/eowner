from django.contrib import admin
from .models import Dailyreports


class DailyreportAdmin(admin.ModelAdmin):
    list_display = ["bus_id", "date", "totalcollection", "wages", "fuel_quantity", "fuel_price", "fuel_total", "company", "address", "phone", "extra_charge", "tyre_charge", "spare_parts", "other_expenses", "net_balance", "staff_det"]


admin.site.register(Dailyreports, DailyreportAdmin)
