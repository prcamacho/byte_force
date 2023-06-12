from django import forms
from .models import Coordinador

class FormCoordinador(forms.Form):
    nombre=forms.CharField(max_length=100, label='Nombres')
    apellido=forms.CharField(max_length=100, label='Apellidos')
    email=forms.EmailField(max_length=100,label='Email')
    dni=forms.IntegerField(label='DNI')
    
class EditarFormCoordinador(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = ["nombre","apellido","email","dni"]
        
    