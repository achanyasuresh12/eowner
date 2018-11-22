from django.contrib import admin
from .models import Businfo


class BusinfoAdmin(admin.ModelAdmin):
    list_display = ["name", "dropping_points", "mgr_id"]


admin.site.register(Businfo, BusinfoAdmin)


