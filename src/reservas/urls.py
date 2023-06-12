from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "reservas"

urlpatterns = [
    path('',listado_reservas,name='listado_reservas'),
    path('nuevo/', nueva_reserva,name='nueva_reserva'),
    path('modificar/<int:id>/', modificar_reserva,name='modificar_reserva'),
    path('listado/',listado_reservas,name='listado_reservas'),
    path('eliminar/<int:id>/',eliminar_reserva,name='eliminar_reserva'),
]