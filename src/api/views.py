from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from servicios.models import *
from .serializers import *
from django.shortcuts import get_object_or_404

@api_view(http_method_names=['GET'])
def lista_servicios(request):
    """
    Devuelve la lista de todos los servicios.
    """
    servicios = Servicio.objects.all()
    serializer = ServicioSerializer(instance=servicios, many=True)
    respuesta = {
        'Mensaje': 'Lista de Servicios',
        'Datos': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_servicio(request, id: int):
    """
    Devuelve los datos de un servicio específico según su ID.
    """
    servicio = get_object_or_404(Servicio, id=id)
    serializer = ServicioSerializer(instance=servicio)
    respuesta = {
        'Datos Servicio': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_clientes(request):
    """
    Devuelve la lista de todos los clientes.
    """
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(instance=clientes, many=True)
    respuesta = {
        'Mensaje': 'Lista de Clientes',
        'Datos': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_cliente(request, id: int):
    """
    Devuelve los datos de un cliente específico según su ID.
    """
    cliente = get_object_or_404(Cliente, id=id)
    serializer = ClienteSerializer(instance=cliente)
    respuesta = {
        'Datos Cliente': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_empleados(request):
    """
    Devuelve la lista de todos los empleados.
    """
    empleados = Empleado.objects.all()
    serializer = EmpleadoSerializer(instance=empleados, many=True)
    respuesta = {
        'Mensaje': 'Lista de Empleados',
        'Datos': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_empleado(request, id: int):
    """
    Devuelve los datos de un empleado específico según su ID.
    """
    empleado = get_object_or_404(Empleado, id=id)
    serializer = EmpleadoSerializer(instance=empleado)
    respuesta = {
        'Datos Empleado': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def lista_coordinadores(request):
    """
    Devuelve la lista de todos los coordinadores.
    """
    coordinadores = Coordinador.objects.all()
    serializer = CoordinadorSerializer(instance=coordinadores, many=True)
    respuesta = {
        'Mensaje': 'Lista de Coordinadores',
        'Datos': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def datos_coordinador(request, id: int):
    """
    Devuelve los datos de un coordinador específico según su ID.
    """
    coordinador = get_object_or_404(Coordinador, id=id)
    serializer = CoordinadorSerializer(instance=coordinador)
    respuesta = {
        'Datos Coordinador': serializer.data
    }
    return Response(data=respuesta, status=status.HTTP_200_OK)
