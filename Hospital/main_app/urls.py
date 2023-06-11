from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("add/clinic",views.add_clinic,name="add_clinic"),
    path("clinics/details/<clinic_id>/", views.clinic_detail, name="clinic_detail"),
    path("clinics/appointment/add/<clinic_id>/", views.make_appointment, name="make_appointment"),
    path("clinics/search/", views.search_page, name="search_page"),
    path('clinics/update/<clinic_id>',views.update_clinic,name="update_clinic"),
    path("clinics/delete/<clinic_id>/", views.delete_clinic, name="delete_clinic"),



]

