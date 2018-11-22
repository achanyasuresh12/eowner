from django.contrib import admin
from .models import Employee


class EmployeAdmin(admin.ModelAdmin):
    list_display = ["empname", "emphouse", "empplace", "empcity", "empemail", "empgender", "empdob", "empcontact", "empdate_of_join", "empqualification", "emp_licence_number", "licence_validity"]


admin.site.register(Employee, EmployeAdmin)

