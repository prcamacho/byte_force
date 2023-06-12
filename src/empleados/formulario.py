from django import forms
from .models import Empleado

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