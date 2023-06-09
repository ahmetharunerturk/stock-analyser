from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.BASE, name='BASE' ),
    path('',views.Home, name='Home' ),
]

