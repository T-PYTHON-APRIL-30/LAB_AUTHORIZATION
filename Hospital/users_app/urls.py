from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),

    path('signin/', views.signin, name = 'signin'),

    path('signout/', views.signout, name = 'signout'),

    path('permission_page/', views.no_permission, name = 'no_permission')
]