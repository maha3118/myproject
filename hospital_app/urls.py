from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('doctors/', views.doctors, name='doctors'),

    path('patients/', views.patients, name='patients'),

    path('appointments/', views.appointments, name='appointments'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('services/', views.services, name='services'),

]