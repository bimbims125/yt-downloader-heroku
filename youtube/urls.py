from django.contrib import admin
from django.urls import path
from ytdonloder import views

urlpatterns = [
    path('', views.ytb_down, name='home'),
]