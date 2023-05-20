from django.urls import path
from . import views

urlpatterns = [
    path('', views.annotation_list, name='annotation_list'),
    path('<int:pk>/', views.annotation_detail, name='annotation_detail'),
]
