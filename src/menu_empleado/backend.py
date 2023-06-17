from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from empleados.models import Empleado


class BackEndEmpleado(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get(Empleado.USERNAME_FIELD)
        if email is None or password is None:
            return
        try:
            user = Empleado._default_manager.get_by_natural_key(email)
        except Empleado.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            Empleado().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            return Empleado.objects.get(pk=user_id)
        except Empleado.DoesNotExist:
            return None        