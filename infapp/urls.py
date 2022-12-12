from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('posts/', views.posts_list, name='posts_list'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]