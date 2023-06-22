from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from empleados.models import Empleado
from coordinadores.models import Coordinador


class BackEndEmpleado(BaseBackend):
    def __init__(self):
        self.mail=None
        self.conta=None
    def authenticate(self, request:HttpRequest , email=None, password=None):
        BackEndEmpleado().mail=email
        BackEndEmpleado().contra=password
        try:
            try:
                user = Empleado.objects.get(email=email,password=password,activo=True)
            except:
                user = Coordinador.objects.get(email=email,password=password,activo=True)      
        except Coordinador.DoesNotExist:
                Coordinador().set_password(password)
                return None  
        return user    

    def get_user(self,user):
        print(BackEndEmpleado().mail)
        print(BackEndEmpleado().conta)
        try:
            try:
                user=Empleado.objects.get(pk=user)
            except:    
                user=Coordinador.objects.get(pk=user)
        except Coordinador.DoesNotExist:
                return None 
        return user        
        
