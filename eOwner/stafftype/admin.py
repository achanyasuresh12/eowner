from django.contrib import admin
from .models import Stafftype


class StafftypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Stafftype, StafftypeAdmin)

