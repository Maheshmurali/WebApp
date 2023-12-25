
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('admins.urls')),
    path('',include('creators.urls')),
    path('',include('user.urls')),
]
