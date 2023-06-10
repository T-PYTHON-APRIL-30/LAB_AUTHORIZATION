from django.urls import path
from . import views

app_name = "clinics_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("clinic/", views.clinics_page, name="clinics_page"),
    path("about/", views.about_page, name="about_page"),
    path("manager/", views.manager_page, name="manager_page"),
    path("clinic/details/<clinic_id>/", views.clinic_detail_page, name="clinic_detail_page"),
    # Clinic
    path("clinic/add/", views.add_clinic_page, name="add_clinic_page"),
    path("clinic/update/<clinic_id>/", views.update_clinic_page, name="update_clinic_page"),
    path("clinic/delete/<clinic_id>/", views.delete_clinic_page, name="delete_clinic_page"),
    path("clinic/manage/",views.clinic_manager_page, name="clinic_manager_page"),
    # Appointment
    path("appointment/manage/", views.appointment_manager_page, name="appointment_manager_page"),
    path("appointment/add/", views.add_appointment_page, name="add_appointment_page"),
    # path("appointment/update/", views.update_appointment_page, name="update_appointment_page"),
]