from typing import Any
from django import forms
from clientes.models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from reservas.models import Reserva
from clientes.models import Cliente
from empleados.models import Empleado
from servicios.models import Servicio
from coordinadores.models import Coordinador
#VALIDACIONES
from .validations import *

# class FormCliente(UserChangeForm):
#     password=None
#     class Meta:
#         model=Cliente
#         fields=[
#             'nombre',
#             'apellido',
#             'email',
#             'dni',
#             'imagen',
#         ]
#         labels={
#             'nombre':'Nombre',
#             'apellido':'Apellido',
#             'email':'Email',
#             'dni':'DNI',
#             'imagen':'Imagen'
#         }
        
#     def clean_dni(self):
#         dni=self.cleaned_data.get('dni')
#         validar_dni(dni)
#         return dni

class FormCliente(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    email=forms.EmailField()
    dni=forms.IntegerField()
    imagen=forms.ImageField(label='Imagen')
    
class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","email","dni","imagen"]    
    
    # def clean_dni(self):
    #     dni=self.cleaned_data.get('dni')
    #     validar_dni(dni)
    #     return dni
        
class AuthCliente(forms.Form):
    dni=forms.IntegerField(label='Ingrese su DNI')   

    
class FormReserva(forms.ModelForm):
    class Meta:
        model= Reserva  
        fields = ['fecha_reserva','responsable','empleado','servicio']
        widgets = {
            'fecha_reserva':forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
        }
    def clean_fecha_reserva(self):
        fecha_reserva = self.cleaned_data['fecha_reserva']
        validar_fecha_posterior(fecha_reserva)
        return fecha_reserva