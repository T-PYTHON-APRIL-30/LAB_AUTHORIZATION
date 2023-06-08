from django.urls import path
from . import views

app_name = "clinics_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
]