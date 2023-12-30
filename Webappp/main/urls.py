from django.urls import path
from . import views

urlpatterns = [
   path('index/',views.index,name='index'),
   path('logout/',views.log_out,name='logout')

]