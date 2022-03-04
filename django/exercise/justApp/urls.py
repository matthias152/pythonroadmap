from django.urls import path, re_path
from justApp import views

urlpatterns = [
    re_path(r'^$', views.users, name='users'),
]
