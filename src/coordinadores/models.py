from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from menu_empleado.models import MyUserManager
class Coordinador(AbstractBaseUser):
    """
    Modelo para representar a un coordinador.

    Atributos:
    - nombre: El nombre del coordinador (máximo 100 caracteres).
    - apellido: El apellido del coordinador (máximo 100 caracteres).
    - email: El correo electrónico del coordinador (máximo 100 caracteres y único).
    - dni: El número de identificación del coordinador (único).
    - activo: Un indicador booleano que representa si el coordinador está activo o no (por defecto, True).
    - fecha_alta: La fecha y hora de alta del coordinador (se establece automáticamente al crear el coordinador).
    """

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    dni = models.BigIntegerField(unique=True)
    activo = models.BooleanField(default=True)
    empleado=models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD='email'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
