from django.core.exceptions import ValidationError
from .models import Servicio
import re

def validar_precio(precio):
    if not str(precio).isdigit():
        raise ValidationError('Solo se permiten números.')