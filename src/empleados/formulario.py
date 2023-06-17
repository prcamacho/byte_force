from django import forms
from .models import Empleado
from django.contrib.auth.forms import UserCreationForm
class FormEmpleado(forms.Form):
    nombre=forms.CharField(max_length=100, label='Nombres')
    apellido=forms.CharField(max_length=100, label='Apellidos')
    email=forms.EmailField(max_length=100,label='Email')
    dni=forms.IntegerField(label='DNI')
    numero_legajo=forms.IntegerField(label='Numero de Legajo')
    
class EditarFormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre","apellido","numero_legajo"]
        
class RegistroEmpleadoForm(UserCreationForm):
    email=forms.EmailField(max_length=100,help_text='Campo Requerido!')
    class Meta:
        model=Empleado
        fields= ["nombre","apellido","numero_legajo",'email','password1','password2']       