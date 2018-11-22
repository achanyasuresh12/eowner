from django.contrib import admin
from .models import Ticketbooking


class TicketbookingAdmin(admin.ModelAdmin):
    list_display = ["date", "source", "destination", "seat", "bus_id", "duration", "dropping_points", "fare", "user_id"]


admin.site.register(Ticketbooking, TicketbookingAdmin)
