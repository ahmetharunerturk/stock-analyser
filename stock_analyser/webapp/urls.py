from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.BASE, name='dashboard' ),
    path('',views.Home, name='Home' ),
    path('features/',views.Features, name='Features' ),
    path('pricing/',views.Pricing, name='Pricing' ),
    path('faqs/',views.FAQs, name='FAQs' ),
    path('about/',views.About, name='About' ),
    path('contact/',views.Contact, name='Contact' ),
]

