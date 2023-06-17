from typing import Any
from django import forms
from clientes.models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from reservas.models import Reserva
from clientes.models import Cliente
from empleados.models import Empleado
from servicios.models import Servicio
from coordinadores.models import Coordinador

class FormCliente(UserChangeForm):
    password=None
    class Meta:
        model=Cliente
        fields=[
            'nombre',
            'apellido',
            'email',
            'dni'
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'dni':'DNI'
        }

class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","email","dni"]    
        
class AuthCliente(forms.Form):
    dni=forms.IntegerField(label='Ingrese su DNI')   

    
class FormReserva(forms.ModelForm):
    class Meta:
        model= Reserva  
        fields = ['fecha_reserva','responsable','empleado','servicio','precio']
        widgets = {
            'fecha_reserva':forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
        }