from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('signin/', views.sign_in, name="sign_in"),
    path('logout/', views.log_out, name="log_out"),
]