
from django.contrib import admin
from .models import Cust


class CustAdmin(admin.ModelAdmin):
    list_display = ["custname", "custage", "custgender", "custemail", "custcontact"]


admin.site.register(Cust, CustAdmin)

