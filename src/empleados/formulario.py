from django import forms
from .models import Empleado
#Validaciones
from .validations import *
from django.contrib.auth.forms import UserCreationForm
class FormEmpleado(forms.Form):
    nombre=forms.CharField(max_length=100, label='Nombres')
    apellido=forms.CharField(max_length=100, label='Apellidos')
    email=forms.EmailField(max_length=100,label='Email')
    dni=forms.IntegerField(label='DNI')
    numero_legajo=forms.IntegerField(label='Numero de Legajo')
    imagen=forms.ImageField()
    
    # def clean_dni(self):
    #     dni = self.cleaned_data.get("dni")
    #     validar_dni(dni)
    #     return dni
    
    # def clean_numero_legajo(self):
    #     legajo = self.cleaned_data.get("numero_legajo")
    #     validar_legajo(legajo)
    #     return legajo
    
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     validar_email(email)
    #     return email
    
class EditarFormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre","apellido","numero_legajo",'imagen']
        
class RegistroEmpleadoForm(UserCreationForm):
    email=forms.EmailField(max_length=100,help_text='Campo Requerido!')
    class Meta:
        model=Empleado
        fields= ["nombre","apellido","numero_legajo",'email','imagen','password1','password2']       