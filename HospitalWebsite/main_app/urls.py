from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('aboutUs/',views.about_us,name="about_us"),
    path('add/clinics/',views.add_clinics,name="add_clinics"),
    path('clinics/<clinic_id>/detail/',views.clinic_detail,name="clinic_detail"),
    path('clinics/update/<clinic_id>/',views.update_clinics,name="update_clinics"),
    path("clinics/search/", views.search_page, name="search_page"),

    path('create/appointment/<clinic_id>/',views.create_appointment,name="create_appointment"),
    path('display/appointment/',views.appointment_list,name="appointment_list"),
    path('update/appointment/<appointment_id>/',views.update_appointment,name="update_appointment"),
    path('delete/appointment/<appointment_id>/',views.delete_appointment,name="delete_appointment"),


]