from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    
    path('clinics/', views.clinics_page, name = 'clinics_page'),
    path('clinics/search/', views.search_page, name = 'search_page'),
    path('clinics/<clinic_id>/', views.clinics_page_detail, name = 'clinics_page_detail'),
    path('clinics/<clinic_id>/booking/', views.booking_page, name = 'booking_page'),
    
    path('manager/', views.manager_page, name = 'manager_page'),
    path('manager/add/', views.manager_page_add, name = 'manager_page_add'),
    path('manager/update/<clinic_id>/', views.manager_page_update, name = 'manager_page_update'),
    
    path('manager/appointments/', views.manager_page_appointments, name = 'manager_page_appointments'),
    path('manager/appointments/add/', views.appointments_page_add, name = 'appointments_page_add'),
    path('manager/appointments/delete/<clinic_id>/', views.appointments_page_delete, name = 'appointments_page_delete'),
    path('manager/appointments/update/<clinic_id>/', views.appointments_page_update, name = 'appointments_page_update')
]