from typing import Any
from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
#Validaciones
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
#             'imagen':'Imagen',
#         }
        
        
#     def clean_dni(self):
#         dni = self.cleaned_data.get("dni")
#         validar_dni(dni)
#         return dni
      
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         validar_email(email)
#         return email

class FormCliente(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    dni = forms.IntegerField(label='DNI')
    imagen=forms.ImageField(label='Imagen')
    
class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","email","dni","imagen"]    
    