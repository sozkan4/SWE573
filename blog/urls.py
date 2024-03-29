from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path


urlpatterns = [
    
    path('', views.home, name='home'),
    path('post/<post_title>', views.view_post, name='view_post'),
    path('post/<post_title>/like', views.like_post, name='like_post'),
    path('post/<str:post_title>/comment',  views.add_comment, name='add_comment'),
    path('profile/<str:user>', views.view_profile, name='profile'),
    path('profile/<str:user>/settings', views.settings, name='settings'),



    path('search/', views.search, name='search'),
    path('update_profile/<current_user>', views.update_profile, name='update_profile'),
    path('change_image/<user>', views.change_image, name='change_image'),
    path('delete_user/<user>', views.delete_user, name='delete_user'),



    path('write_post/', views.write_post, name='write_post'),
    path('post_created/', views.post_created, name='post_created'),
    path('delete/<post_title>', views.delete_post, name='delete_post'),
    path('annotations/', include('annotations.urls')),






    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)