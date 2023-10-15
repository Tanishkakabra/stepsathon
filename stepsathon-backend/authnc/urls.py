from django.contrib import admin
from django.urls import path
from .views import login, RegisterView


urlpatterns = [
    path('login/', login), 
    path('signup/', RegisterView)
]