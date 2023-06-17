from django import forms
from django.utils import timezone

def validar_fecha_posterior(value):
    print(f" VALUE{value}")
    print(f" TIME ZONE{timezone.now()}")
    if value <= timezone.now():
        raise forms.ValidationError("La fecha de reserva debe ser posterior a hoy.")
