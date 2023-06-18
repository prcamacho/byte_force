from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
from django.contrib.auth.models import UserManager,BaseUserManager
#from menu_empleado.models import MyUserManager
#Modelo del objeto Empleado

# class MyUserManager(BaseUserManager):
    
#     def create_user(self, email, nombre,apellido,dni, password=None):
#         if not email:
#             raise ValueError('Email requerido!')
#         if not nombre:
#             raise ValueError('Nombre requerido!')
#         if not apellido:
#             raise ValueError('Apellido requerido!')
#         if not dni:
#             raise ValueError('DNI requerido!')
#         user = self.model(email=self.normalize_email(email),
#                           nombre=nombre, 
#                           apellido=apellido,)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email,nombre,apellido, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             nombre=nombre, 
#             apellido=apellido,
#             password=password,)
#         user.is_admin = True
#         user.is_staff=True
#         user.is_superuser= True
#         user.save(using=self._db)
#         return user

class Empleado(AbstractBaseUser):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(verbose_name='email',max_length=100,unique=True)
    dni= models.BigIntegerField(unique=True)
    numero_legajo=models.PositiveIntegerField(unique=True)
    activo=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    empleado=models.BooleanField(default=True)
    fecha_alta=models.DateTimeField(auto_now_add=True)
        
    objects = UserManager()    
        
    USERNAME_FIELD='email'
   
   
        
    
