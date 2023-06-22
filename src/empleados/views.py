from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .formulario import FormEmpleado, EditarFormularioEmpleado
from .models import Empleado
from django.contrib import messages
from django.forms import ModelForm
import time
from reservas.models import Reserva

def nuevo_empleado(request):
    """
    Vista para crear un nuevo empleado.

    Permite agregar un empleado mediante el formulario proporcionado.
    Si los datos son válidos, se crea un nuevo objeto Empleado con los valores proporcionados.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Si la solicitud es GET, renderiza el formulario vacío.
    - Si la solicitud es POST y los datos del formulario son válidos, redirige a la página de listado de empleados.
    - Si la solicitud es POST y los datos del formulario no son válidos, renderiza el formulario con los errores.

    Plantilla:
    - empleados/nuevo.html
    """
    if request.user.is_authenticated and request.user.empleado == True:
        if request.method == "POST":
            formulario = FormEmpleado(request.POST, request.FILES)
            if formulario.is_valid():
                cd = formulario.cleaned_data
                Empleado.objects.create(
                    nombre=cd['nombre'],
                    apellido=cd['apellido'],
                    email=cd['email'],
                    dni=cd['dni'],
                    numero_legajo=cd['numero_legajo']
                )
                time.sleep(1.5)
                return HttpResponseRedirect("/administracion/empleados/listado/")
        else:
            formulario = FormEmpleado()
        return render(request, 'empleados/nuevo.html', {"form": formulario})
    else:
        return redirect('/administracion/login/')

def modificar_empleado(request, id):
    """
    Vista para modificar un empleado existente.

    Permite editar los datos de un empleado existente mediante el formulario proporcionado.
    Si los datos son válidos, se actualiza el objeto Empleado con los nuevos valores.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del empleado a modificar.

    Retorna:
    - Si la solicitud es GET, renderiza el formulario con los datos del empleado.
    - Si la solicitud es POST y los datos del formulario son válidos, redirige a la página de listado de empleados.
    - Si la solicitud es POST y los datos del formulario no son válidos, renderiza el formulario con los errores.

    Plantilla:
    - empleados/nuevo.html
    """
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = get_object_or_404(Empleado, id=id)
        if request.method == 'POST':
            formulario = EditarFormularioEmpleado(request.POST, request.FILES, instance=empleado)
            if formulario.is_valid():
                formulario.save()
                time.sleep(1.5)
                return HttpResponseRedirect("/administracion/empleados/listado/")
        else:
            formulario = EditarFormularioEmpleado(instance=empleado)
        return render(request, 'empleados/nuevo.html', {'form': formulario})
    else:
        return redirect('/administracion/login/')
    
def activar_empleado(request, id):
    """
    Vista para activar un empleado desactivado.

    Permite activar un empleado desactivado cambiando el estado "activo" a True.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del empleado a activar.

    Retorna:
    - Redirige a la página de listado de empleados.

    Plantilla:
    - No se utiliza.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = get_object_or_404(Empleado, id=id)
        if empleado.activo == False:
            empleado.activo = True
            empleado.save()
        return HttpResponseRedirect("/administracion/empleados/listado/")
    else:
        return redirect('/administracion/login/')

def desactivar_empleado(request, pk):
    """
    Vista para desactivar un empleado activo.

    Permite desactivar un empleado activo cambiando el estado "activo" a False.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - pk: El ID del empleado a desactivar.

    Retorna:
    - Redirige a la página de listado de empleados.

    Plantilla:
    - No se utiliza.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = get_object_or_404(Empleado, id=pk)
        empleado.activo = False
        empleado.save()
        return HttpResponseRedirect("/administracion/empleados/listado/")
    else:
        return redirect('/administracion/login/')


def listado_empleados(request):
    """
    Vista para mostrar el listado de empleados.

    Obtiene todos los empleados registrados y los pasa como contexto a la plantilla de listado.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Renderiza la plantilla de listado de empleados con el contexto.

    Plantilla:
    - empleados/listado.html
    """
    if request.user.is_authenticated and request.user.empleado == True:
        empleados = Empleado.objects.all()
        return render(request, 'empleados/listado.html', {'empleados': empleados})
    else:
        return redirect('/administracion/login/')
    
def mostrar_empleado(request,id):
    if request.user.is_authenticated and request.user.empleado == True:
        empleado=get_object_or_404(Empleado,id=id)
        eventos=Reserva.objects.filter(empleado=empleado)   
        return render(request, 'empleados/mostrar_empleado.html',{'empleado':empleado,'eventos':eventos})
    else:
        return redirect('/administracion/login/')    
    