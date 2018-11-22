from django.contrib import admin
from .models import Managers


class ManagerAdmin(admin.ModelAdmin):
    list_display = ["mgrname", "mgrhouse", "mgrplace", "mgrcity", "mgremail", "mgrgender", "mgrdob", "mgrcontact", "mgrusername", "mgrpassword", "mgrdate_of_join", "mgrqualification"]


admin.site.register(Managers, ManagerAdmin)

