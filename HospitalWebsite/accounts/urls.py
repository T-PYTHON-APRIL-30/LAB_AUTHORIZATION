from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="log_in"),
    path('logout/', views.log_out, name="log_out"),
    path('no/permission/', views.no_permission_page, name="no_permission_page"),
]