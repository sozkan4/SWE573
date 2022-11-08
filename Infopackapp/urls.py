from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Infopack.urls'))
]

from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    ...
    path("register", views.register_request, name="register")
]