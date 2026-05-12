from django.contrib import admin
from .models import Doctor, Patient, Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'phone')
    search_fields = ('name',)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'disease')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)