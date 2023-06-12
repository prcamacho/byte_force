from typing import Any
from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm

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
        
       
# class FormCliente(forms.Form):
#     nombre=forms.CharField(max_length=100, label='Nombres')
#     apellido=forms.CharField(max_length=100, label='Apellidos')
#     email=forms.EmailField(max_length=100,label='Email')
#     dni=forms.IntegerField(label='DNI')
    
class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","email","dni"]    
        
class AuthCliente(forms.Form):
    dni=forms.IntegerField(label='Ingrese su DNI')        