from django.contrib import admin
from .models import Bookbus


class BookbusAdmin(admin.ModelAdmin):
    list_display = ["source", "destination", "date"]


admin.site.register(Bookbus, BookbusAdmin)
