from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signin/', views.signin, name="sign_in"),
    path('signup/', views.signup, name="signup"),
    path('user/logout/', views.logout_view, name="log_out"),
]