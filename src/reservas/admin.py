from django.contrib import admin
from .models import Reserva
# Register your models here.

class AdminReserva(admin.ModelAdmin):
    list_display = ('cliente','responsable','empleado','servicio','precio','fecha_reserva','fecha_creacion')
    search_fields=['coordinador','cliente','empleado','servicio']


admin.site.register(Reserva,AdminReserva)
