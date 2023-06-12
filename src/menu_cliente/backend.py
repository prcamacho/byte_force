from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from clientes.models import Cliente


class BackEndCliente(BaseBackend):
    def authenticate(self, request: HttpRequest, dni: str):
        try:
            cliente = Cliente.objects.get(dni=dni,activo=True)
            if cliente.activo==False:
                raise ValueError("el cliente no está activo, comuniquese con el programador")
        except Cliente.DoesNotExist:
            return None
        #     # Crea un nuevo usuario. No es necesario establecer una contraseña
        #     # porque solo se comprueba la contraseña de settings.py.
        #     cliente = Cliente(username=username)
        #     cliente.is_staff = True
        #     cliente.is_superuser = True
        #     cliente.save()
        # return cliente
        return cliente

    def get_user(self, user_id):
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None        