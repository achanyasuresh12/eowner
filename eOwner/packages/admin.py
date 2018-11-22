from django.contrib import admin
from .models import Packages


class PackagesAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "seatcount", "rate", "description", "mgr_id"]


admin.site.register(Packages, PackagesAdmin)
