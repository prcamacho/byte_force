from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Cliente(AbstractBaseUser):
    """
    Modelo para representar a un cliente.

    Atributos:
    - nombre: El nombre del cliente (máximo 100 caracteres).
    - apellido: El apellido del cliente (máximo 100 caracteres).
    - email: El correo electrónico del cliente (máximo 100 caracteres y único).
    - dni: El número de identificación del cliente (único).
    - activo: Un indicador booleano que representa si el cliente está activo o no (por defecto, True).
    - fecha_alta: La fecha y hora de alta del cliente (se establece automáticamente al crear el cliente).
    """

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    dni = models.BigIntegerField(unique=True)
    activo = models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    empleado=models.BooleanField(default=False)
    
    USERNAME_FIELD = 'dni'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'
