from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = "administracion"

urlpatterns = [
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('',menu_administracion,name='menu_administracion')
]