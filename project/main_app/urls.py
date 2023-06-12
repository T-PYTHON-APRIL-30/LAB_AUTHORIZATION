from django.urls import path
from . import views
app_name = 'main_app'

urlpatterns = [


    path('' , views.home, name= 'home'),

    path('clinic_list/' , views.clinic_list, name= 'clinic_list'),
    path('<int:id>/clinic_detail/', views.clinic_detail, name='clinic_detail'),
    path('add_clinic/' , views.add_clinic, name= 'add_clinic'),
    path('clinic_delete/<int:id>/', views.clinic_delete, name='clinic_delete'),
    path("search/", views.search_page, name="search_page"),


]