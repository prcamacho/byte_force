from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class Cliente(AbstractBaseUser):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    dni= models.BigIntegerField(unique=True)
    activo=models.BooleanField(default=True)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    empleado=models.BooleanField(default=False)
    
    USERNAME_FIELD='dni'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'
