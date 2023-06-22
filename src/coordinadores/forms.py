from django import forms
from .models import Coordinador
from .validations import *

class FormCoordinador(forms.Form):
    nombre=forms.CharField(max_length=100, label='Nombres')
    apellido=forms.CharField(max_length=100, label='Apellidos')
    email=forms.EmailField(max_length=100,label='Email')
    dni=forms.IntegerField(label='DNI')
    imagen=forms.ImageField(label='Imagen')
    
    # def clean_dni(self):
    #     dni = self.cleaned_data.get("dni")
    #     validar_dni(dni)
    #     return dni
      
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     validar_email(email)
    #     return email
    
class EditarFormCoordinador(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = ["nombre","apellido","dni",'imagen']
        
    