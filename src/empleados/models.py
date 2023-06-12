from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

#Modelo del objeto Empleado

class Empleado(AbstractBaseUser):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    dni= models.BigIntegerField(unique=True)
    numero_legajo=models.PositiveIntegerField(unique=True)
    activo=models.BooleanField(default=True)
    fecha_alta=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'
    
