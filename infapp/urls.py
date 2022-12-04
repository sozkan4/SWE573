from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
]