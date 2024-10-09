from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up),
    path('login', views.login),
    path('verify_login', views.verify_login),
    path('verify_signup', views.verify_signup),
]