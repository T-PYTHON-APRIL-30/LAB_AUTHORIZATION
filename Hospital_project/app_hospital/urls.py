from django.urls import path
from . import views

app_name = "app_hospital"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("all_detials", views.clinics_detials, name="clinic_detials"),
    path("detial/<clinic_id>/", views.clinic_detials, name="one_clinic_detials"),
    path("search/", views.search_page, name="search_page"),
    path("add/clinic/", views.add_clinic, name="add_clinic"),
    path("update/clinic/<clinic_id>", views.update_clinic, name="update_clinic"),
    path("add/appointment/<clinic_id>",views.add_appointment, name="add_appointment"),

]
