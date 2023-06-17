from django.core.exceptions import ValidationError
from django.utils import timezone
import re

from .models import Empleado


def validar_dni(dni):
    if len(str(dni)) != 8 or dni <= 0:
        raise ValidationError('El DNI debe ser un número positivo de 8 dígitos positivo.')
    if Empleado.objects.filter(dni=dni).exists():
        raise ValidationError('Ya existe un empleado con ese DNI.')
    
def validar_legajo(legajo):
    if len(str(legajo)) != 10 or legajo <= 0:
        raise ValidationError('El Legajo  debe ser un número positivo de 10 dígitos positivo.')
    
    if Empleado.objects.filter(numero_legajo=legajo).exists():
        raise ValidationError('Ya existe un empleado con ese Legajo.')

def validar_email(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError('El correo electrónico no es inválido.')
    if Empleado.objects.filter(email = email).exists():
        raise ValidationError('El correo electrónico ya existe.')

