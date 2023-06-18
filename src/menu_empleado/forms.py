from typing import Any
from django import forms
from clientes.models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from reservas.models import Reserva
from clientes.models import Cliente
from empleados.models import Empleado
from servicios.models import Servicio
from coordinadores.models import Coordinador

class AuthEmpleado(forms.Form):
    email=forms.EmailField(label='Ingrese su Email')  
    password = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
