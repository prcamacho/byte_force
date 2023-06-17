from django.db import models
from django.contrib.auth.models import UserManager,BaseUserManager
#Modelo del objeto Empleado

class MyUserManager(BaseUserManager):
    
    def create_user(self, email, nombre,apellido,dni, password=None):
        if not email:
            raise ValueError('Email requerido!')
        if not nombre:
            raise ValueError('Nombre requerido!')
        if not apellido:
            raise ValueError('Apellido requerido!')
        if not dni:
            raise ValueError('DNI requerido!')
        user = self.model(email=self.normalize_email(email),
                          nombre=nombre, 
                          apellido=apellido,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,nombre,apellido, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nombre=nombre, 
            apellido=apellido,
            password=password,)
        user.is_admin = True
        user.is_staff=True
        user.is_superuser= True
        user.save(using=self._db)
        return user