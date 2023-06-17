from django.core.exceptions import ValidationError
from .models import Coordinador
import re

def validar_dni(dni):
    if len(str(dni)) != 8 or dni <= 0:
        raise ValidationError('El DNI debe ser un número positivo de 8 dígitos positivo.')
    if Coordinador.objects.filter(dni=dni).exists():
        raise ValidationError('Ya existe un empleado con ese DNI.')
    

def validar_email(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError('El correo electrónico no es inválido.')
    if Coordinador.objects.filter(email = email).exists():
        raise ValidationError('El correo electrónico ya existe.')