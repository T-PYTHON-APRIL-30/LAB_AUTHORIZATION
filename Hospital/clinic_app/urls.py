from django.urls import path
from . import views

app_name = "clinic_app"

urlpatterns = [
    path("home/", views.home, name = "home"),
]