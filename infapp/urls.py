from django.urls import path
from . import views

urlpatterns = [
    path('Infapp/', views.index, name='infapp'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
]