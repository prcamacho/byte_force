from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = "clientes"

urlpatterns = [
    path('',listado_clientes,name='listado_clientes'),
    path('nuevo/',nuevo_cliente,name='nuevo_cliente'),
    path('desactivar/<int:id>/',desactivar_cliente,name='desactivar_cliente'),
    path('activar/<int:id>/',activar_cliente,name='activar_cliente'),
    path('listado/',listado_clientes,name='listado_clientes'),
    path('modificar/<int:id>/',modificar_cliente,name='modificar_cliente'),
]