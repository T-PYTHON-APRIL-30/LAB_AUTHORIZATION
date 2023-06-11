from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("clinic/add/", views.add_update_clinic, name="add_update_clinic"),
    path("clinic/detail/<clinic_id>/", views.detail, name="detail"),
    path("clinic/search/", views.search, name="search"),
    path("clinic/update/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("clinic/<clinic_id>/book/add/", views.book_appointment, name="book_appointment"),
    path("clinic/search/", views.search, name="search"),


]