from django.contrib import admin
from django.urls import path
from homeApp import views

urlpatterns = [
    path('', views.home_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path( 'displayDay/<str:day>', views.day_view)
]