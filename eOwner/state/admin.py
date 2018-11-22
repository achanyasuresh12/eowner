from django.contrib import admin
from .models import State


class StateAdmin(admin.ModelAdmin):
    list_display = ["state_name"]


admin.site.register(State, StateAdmin)
