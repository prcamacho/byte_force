from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = "menu"

urlpatterns = [
    path('registro/',registrar_cliente,name='registrar_cliente'),
    path('modificar/',modificar_cliente,name='modificar_cliente'),
    path('login',log_in,name='log_in'),    
    path('logout/',log_out,name='log_out'),
    path('',reservas_user_cliente,name='reservas_user_cliente'),
    path('desactivar/<int:pk>',desactivar_reserva,name='desactivar_reserva'),
    path('editar/<int:id>',modificar_reserva_user,name="modificar_reserva_user"),
    path('nuevo/',hacer_reserva,name='hacer_reserva'),
]