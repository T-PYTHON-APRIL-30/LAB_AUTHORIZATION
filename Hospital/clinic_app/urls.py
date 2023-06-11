from django.urls import path
from . import views

app_name = "clinic_app"

urlpatterns = [
    path("home/", views.home, name = "home"),
    path('add/clinic', views.add_clinic, name='add_clinic'),
    path('clinic/details/<clinic_id>/', views.clinic_details, name='clinic_details'),
    path("search/", views.search, name="search"),
    path("update/clinic/<clinic_id>/", views.update_clinic, name="update_clinic"),

]