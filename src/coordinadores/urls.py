from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "coordinadores"


urlpatterns = [
    path('',listado_coordinadores,name='listado_coordinadores'),
    path('activar/<int:id>/',activar_coordinador,name='activar_coordinador'),
    path('desactivar/<int:id>/',desactivar_coordinador,name='desactivar_coordinador'),
    path('listado/',listado_coordinadores,name='listado_coordinadores'),
    path('nuevo/',nuevo_coordinador,name='nuevo_coordinador'),
    path('modificar/<int:id>',modificar_coordinador,name='modificar_coordinador'),
    path('mostrar/<int:id>',mostrar_coordinador,name='mostrar_coordinador'),
]