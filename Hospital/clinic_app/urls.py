from django.urls import path
from . import views

app_name = "clinic_app"

urlpatterns = [
    path("", views.home, name = "home"),
    path('add/clinic', views.add_clinic, name='add_clinic'),
    path('clinic/details/<clinic_id>/', views.clinic_details, name='clinic_details'),
    path("search/", views.search, name="search"),
    path("update/clinic/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("contact/", views.contact, name="contact"),
    path("appointment/<clinic_id>/", views.appointment_page, name="appointment"),
    path('create/appointment/<clinic_id>/', views.create_appointment, name='create_appointment'),
    path('not/found/', views.not_found, name="not_found"),

]