from django.urls import path
from . import views
app_name="hospital_app"

urlpatterns = [
    path('', views.index_page, name="index_page"),
    path('clinics/add', views.add_clinics, name="add_clinics"),
    path("clinics/<clinic_id>/details/", views.detail_page, name="detail_page"),
    path('clinics/update/<clinic_id>',views.update_page,name="update_page"),
    path('search/',views.search_page,name="search_page"),
    path('clinics/manager/' ,views.manager_page,name="manager_page"),
    path('clinics/add/appointment/<clinic_id>' ,views.add_appointment,name="add_appointment"),
    path('clinics/view/appointment/<clinic_id>',views.view_appointment,name="view_appointment"),
    path('clinics/delete/<clinic_id>',views.delete_clinics,name="delete_clinics"),
    path('clinics/manager/appointment/<clinic_id>',views.manage_appointment,name="manage_appointment"),
    path('clinics/manager/appointment/<clinic_id>/attended/<appointment_id>',views.patient_attended,name="patient_attended"),
    path('clinics/manager/appointment/<clinic_id>/not/attended/<appointment_id>',views.patient_notattended,name="patient_notattended"),
    path('clinics/manager/appointment/<clinic_id>/delete/<appointment_id>',views.delete_appointent,name="delete_appointent"),
    path('clinics/manager/appointment/<clinic_id>/update/<appointment_id>',views.update_appointent,name="update_appointent"),

    path('signup/', views.sign_up, name="sign_up"),
    path('signin/', views.sign_in, name="sign_in"),
    path('logout/', views.log_out, name="log_out"),
    path('no/permission/', views.no_permission_page, name="no_permission_page"),
    
]
