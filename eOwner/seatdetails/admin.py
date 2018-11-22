from django.contrib import admin
from .models import SeatDet


class SeatinfoAdmin(admin.ModelAdmin):
    list_display = ["bus_id", "Seat_name", "rate", "status"]


admin.site.register(SeatDet, SeatinfoAdmin)
