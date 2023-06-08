from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('register/', views.register_page, name = 'register_page'),
    
    path('login/', views.login_page, name = 'login_page'),
    
    path('logout/', views.logout_page, name = 'logout_page'),
]