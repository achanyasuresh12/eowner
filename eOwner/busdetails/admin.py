from django.contrib import admin
from .models import Busdetails


class BusdetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "regno", "permitno", "seat", "source", "destination", "description", "arrival_time", "departure_time", "seatorder", "mgr_id"]


admin.site.register(Busdetails, BusdetailsAdmin)
