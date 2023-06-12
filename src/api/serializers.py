from rest_framework import serializers
from clientes.models import Cliente
from coordinadores.models import Coordinador
from empleados.models import Empleado
from servicios.models import Servicio
from servicios.models import *

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields=['id','nombre','precio']
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['id','nombre','apellido']
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=['id','nombre','apellido','numero_legajo']
        
class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coordinador
        fields=['id','nombre','apellido','numero_documento','fecha_alta']                        