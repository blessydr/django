from django.contrib import admin
from django.urls import path
from my_apps import views

urlpatterns = [
   path('',views.home),
   path('register',views.register)
]