from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser
# Create your models here.

#Modelo del objeto Empleado

class Empleado(AbstractBaseUser):
    """
    Modelo para representar un empleado.

    Atributos:
    - nombre: El nombre del empleado.
    - apellido: El apellido del empleado.
    - email: El correo electrónico del empleado (debe ser único).
    - dni: El número de identificación del empleado (debe ser único).
    - numero_legajo: El número de legajo del empleado (debe ser único).
    - activo: Indica si el empleado está activo o no.
    - fecha_alta: La fecha de alta del empleado.

    Métodos:
    - __str__: Retorna una representación legible en forma de cadena del empleado.

    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    dni = models.BigIntegerField(unique=True)
    numero_legajo = models.PositiveIntegerField(unique=True)
    activo = models.BooleanField(default=True)
    empleado=models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)

    objects = UserManager() 

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'
