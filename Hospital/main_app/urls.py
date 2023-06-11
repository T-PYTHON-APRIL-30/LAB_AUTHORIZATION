from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [ path('',views.homePage, name = 'homePage'),
               path('clinics/add/',views.addClinic, name='addClinic'),
               path("clinics/details/<clinic_id>/", views.clinic_detail, name="clinic_detail"),
               path("clinics/update/<clinic_id>/", views.update_clinic, name="update_clinic"),
               path("clinics/delete/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
               path("clinics/<clinic_id>/appointment/book/", views.book_appointment, name="book_appointment"),
               path('clinics/search/',views.searchPage, name='searchPage'),

]