from django.contrib import admin
from .models import Feedback


class FeeadbackAdmin(admin.ModelAdmin):
    list_display = ["feedbackcontent", "bus_id", "user_id"]


admin.site.register(Feedback, FeeadbackAdmin)
