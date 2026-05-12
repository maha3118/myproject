from django.shortcuts import render
from .models import Doctor, Patient, Appointment


# Home
def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})


# Doctors
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})


# Patients
def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})


# Appointments
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})


# About
def about(request):
    return render(request, 'about.html')


# Contact
def contact(request):
    return render(request, 'contact.html')


# Services
def services(request):
    return render(request, 'services.html')