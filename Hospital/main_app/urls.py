from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('clinics/', views.clinics, name = 'clinics'),
    path('clinics/search/', views.search, name = 'search'),
    path('clinics/<int:clinic_id>/', views.clinics_detail, name = 'clinics_detail'),
    path('clinics/<clinic_id>/booking/', views.booking, name = 'booking'),
    path('clinics/manager/', views.manager, name = 'manager'),
    path('clinics/manager/add/', views.manager_add, name = 'manager_add'),
    path('clinics/manager/update/<clinic_id>/', views.manager_update, name = 'manager_update'),
    path('clinics/manager/appointments/', views.manager_appointments, name = 'manager_appointments'),
    path('clinics/manager/appointments/add/', views.appointments_add, name = 'appointments_add'),
    path('clinics/manager/appointments/delete/<appointment_id>/', views.appointments_delete, name = 'appointments_delete'),
    path('clinics/manager/appointments/update/<appointment_id>/', views.appointments_update, name = 'appointments_update')
]