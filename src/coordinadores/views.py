from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Coordinador
from django.contrib import messages
from .forms import EditarFormCoordinador, FormCoordinador

def activar_coordinador(request, id):
    """
    Activa un coordinador existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del coordinador a activar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de coordinadores.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        coordinador_a_activar = get_object_or_404(Coordinador, id=id)
        coordinador_a_activar.activo = True
        coordinador_a_activar.save()
        return redirect(reverse('coordinadores:listado_coordinadores'))
    else:
        return redirect('/administracion/login/')

def desactivar_coordinador(request, id):
    """
    Desactiva un coordinador existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del coordinador a desactivar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de coordinadores.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        coordinador_a_desactivar = get_object_or_404(Coordinador, id=id)
        coordinador_a_desactivar.activo = False
        coordinador_a_desactivar.save()
        return redirect(reverse('coordinadores:listado_coordinadores'))
    else:
        return redirect('/administracion/login/')

def listado_coordinadores(request):
    """
    Muestra el listado de coordinadores.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Devuelve:
    - Una respuesta HTTP renderizando el listado de coordinadores.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        coordinadores = Coordinador.objects.all()
        return render(request, 'coordinadores/listado.html', {'coordinadores': coordinadores})
    else:
        return redirect('/administracion/login/')

def nuevo_coordinador(request):
    """
    Crea un nuevo coordinador con los datos proporcionados en el formulario.
    Redirige al listado de coordinadores después de crear el coordinador.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de coordinadores.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        form = FormCoordinador()
        mensaje = None
        coordinador_nuevo = None
        if request.method == 'POST':
            form = FormCoordinador(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                coordinador_nuevo = Coordinador.objects.create(
                    nombre=cd['nombre'],
                    apellido=cd['apellido'],
                    email=cd['email'],
                    dni=cd['dni']
                )
                return HttpResponseRedirect("/administracion/coordinadores/listado/")
        else:
            form = FormCoordinador()
        return render(request, 'coordinadores/nuevo.html', {'form': form})
    else:
        return redirect('/administracion/login/')

def modificar_coordinador(request, id):
    """
    Modifica un coordinador existente con los datos proporcionados en el formulario.
    Redirige al listado de coordinadores después de modificar el coordinador.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del coordinador a modificar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de coordinadores.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        coordinador = get_object_or_404(Coordinador, id=id)
        if request.method == 'POST':
            formulario = EditarFormCoordinador(request.POST, instance=coordinador)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/administracion/coordinadores/listado/")
        else:
            formulario = EditarFormCoordinador(instance=coordinador)
        return render(request, 'coordinadores/nuevo.html', {'form': formulario})
    else:
        return redirect('/administracion/login/')
