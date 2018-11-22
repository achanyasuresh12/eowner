from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["complaintcontent", "bus_id", "user_id"]


admin.site.register(Complaint, ComplaintAdmin)

