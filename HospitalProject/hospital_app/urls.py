from django.urls import path
from . import views

app_name ='hospital_app'

urlpatterns = [
    path('home/',views.home_page , name ="home_page"),
    path('clinic/details/<clinic_id>/', views.clinic_details, name ="clinic_details"),
    path('add/clinic/', views.add_clinic, name ="add_clinic"),
    path("clinic/search/", views.search_page, name="search_page"),
    path("clinic/update/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("clinic/delete/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
    path("clinic/<clinic_id>/book/appointment/", views.book_appointment, name="book_appointment"),
    path('clinic/details/appointment/<appointment_id>/', views.appointment_details, name ="appointment_details"),
    path("appointment/update/<appointment_id>/", views.update_appointment, name="update_appointment"),

]