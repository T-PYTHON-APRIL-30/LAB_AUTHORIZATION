from django.urls import path
from . import views


app_name = 'appointment'

urlpatterns = [

    
    path('appointment_list/' , views.appointment_list, name= 'appointment_list'),
    path('<int:id>/appointment_detail/', views.appointment_detail, name='appointment_detail'),
    path('add_Appointment/<int:id>/' , views.add_Appointment, name= 'add_Appointment'),
    path('appointment_list_category/<str:department>/' , views.appointment_list_category, name= 'appointment_list_category'),
    path('appointment_delete/<int:id>/', views.appointment_delete, name='appointment_delete'),
    
]