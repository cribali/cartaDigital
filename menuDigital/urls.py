
from django.contrib import admin
from django.urls import path,include
from carta import views

urlpatterns = [
     path('', include('carta.urls')),
    path('', views.Bienvenida)
]
