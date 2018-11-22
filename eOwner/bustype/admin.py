from django.contrib import admin
from .models import Bustype


class BustypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Bustype, BustypeAdmin)

