from django.contrib import admin
from  .models import  Branchdetails


class BranchdetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "district", "state", "email", "contact", "type"]


admin.site.register(Branchdetails, BranchdetailsAdmin)
