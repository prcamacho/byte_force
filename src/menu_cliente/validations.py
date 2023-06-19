from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
from reservas.models import Reserva


def validar_fecha_posterior(fecha_reserva):
    if fecha_reserva < timezone.now():
        raise ValidationError("La fecha de reserva debe ser posterior a la fecha actual.")
    
    fecha_reserva_date = fecha_reserva.datetime()
    reservas_mismo_dia = Reserva.objects.filter(fecha_reserva=fecha_reserva_date)
    
    if reservas_mismo_dia.exists():
        raise ValidationError("Ya existe una reserva para la fecha seleccionada.")


    
def validar_dni(dni):
    if len(str(dni)) != 8 or dni <= 0:
        raise ValidationError('El DNI debe ser un número positivo de 8 dígitos.')

