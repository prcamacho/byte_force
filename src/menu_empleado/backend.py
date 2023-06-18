from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from empleados.models import Empleado
from coordinadores.models import Coordinador


class BackEndEmpleado(BaseBackend):
    def authenticate(self, request:HttpRequest , email=None, password=None):
        try:
            try:
                user = Empleado.objects.get(email=email,password=password,activo=True)
            except:
                user = Coordinador.objects.get(email=email,password=password,activo=True)      
        except Coordinador.DoesNotExist:
                Coordinador().set_password(password)
                return None
        return user    

    def get_user(self, user_id):
        try:
            try:
                return Empleado.objects.get(pk=user_id)
            except Empleado.DoesNotExist:
                return None   
        except:   
            try:
                return Coordinador.objects.get(pk=user_id)
            except Coordinador.DoesNotExist:
                return None     
        
