from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up),
    path('login', views.login),
]