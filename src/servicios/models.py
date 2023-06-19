from django.db import models

# Create your models here.

class Servicio(models.Model):
    """
    Modelo para representar un servicio.

    Un servicio tiene un nombre, una descripción opcional, un precio y un estado de activo.
    """

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    activo = models.BooleanField(default=True)

    def __str__(self):
        """
        Devuelve una representación en cadena del servicio.

        El formato de la cadena es el nombre del servicio.
        """
        return f"{self.nombre.upper()} ${self.precio}"
