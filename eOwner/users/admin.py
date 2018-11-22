from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["psgname", "psgage", "psggender", "psgemail", "psgcontact", "psgusername", "psgpassword"]


admin.site.register(User, UserAdmin)

