from django.contrib import admin
from main.models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','mobile_no','detail','precaution','visit_date','next_visit_date')
    search_fields = ('full_name','mobile_no')
admin.site.register(Patient,PatientAdmin)
