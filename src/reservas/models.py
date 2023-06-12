from django.db import models
from clientes.models import Cliente
from coordinadores.models import Coordinador
from empleados.models import Empleado
from servicios.models import Servicio

# Create your models here.
class Reserva(models.Model):
    """
    Modelo para representar una reserva.

    Una reserva contiene la fecha de creación, fecha de reserva, cliente, responsable,
    empleado, servicio y precio.

    """
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_reserva = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    responsable = models.ForeignKey(Coordinador, on_delete=models.DO_NOTHING)
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING)
    servicio = models.ForeignKey(Servicio, on_delete=models.DO_NOTHING)
    precio = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Reserva #{self.id}'
