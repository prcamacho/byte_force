from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .models import Servicio
from .forms import FormularioServicio, EditarFormularioServicio

# Create your views here.

def nuevo_servicio(request):
    """
    Vista para crear un nuevo servicio.

    Permite crear un nuevo servicio con nombre, descripción y precio.
    Después de crear el servicio, redirige al listado de servicios.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        form = FormularioServicio()
        if request.method == 'POST':
            form = FormularioServicio(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Servicio.objects.create(nombre=cd['nombre'],
                                        descripcion=cd['descripcion'],
                                        precio=cd['precio']
                )
                return HttpResponseRedirect("/administracion/servicios/listado")           
        return render(request, 'servicios/nuevo.html', {'form': form})
    else:
        return redirect('/administracion/login')

def modificar_servicio(request, id):
    """
    Vista para modificar un servicio existente.

    Permite modificar el nombre, descripción y precio de un servicio existente.
    Después de modificar el servicio, redirige al listado de servicios.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        servicio = get_object_or_404(Servicio, id=id)
        if request.method == 'POST':
            formulario = EditarFormularioServicio(request.POST, instance=servicio)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/administracion/servicios/listado")
        else:
            formulario = EditarFormularioServicio(instance=servicio)
            return render(request, 'servicios/nuevo.html', {'form': formulario}) 
    else:
        return redirect('/administracion/login')

def desactivar_servicio(request, pk):
    """
    Vista para desactivar un servicio.

    Permite desactivar un servicio existente.
    Después de desactivar el servicio, redirige al listado de servicios.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        servicio = get_object_or_404(Servicio, id=pk)
        if servicio.activo == True:
            servicio.activo = False
            servicio.save()
        return HttpResponseRedirect("/administracion/servicios/listado")
    else:
        return redirect('/administracion/login')

def activar_servicio(request, pk):
    """
    Vista para activar un servicio.

    Permite activar un servicio desactivado.
    Después de activar el servicio, redirige al listado de servicios.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        servicio = get_object_or_404(Servicio, id=pk)
        if servicio.activo == False:
            servicio.activo = True
            servicio.save()
        return HttpResponseRedirect("/administracion/servicios/listado")
    else:
        return redirect('/administracion/login')

def listado_servicios(request):
    """
    Vista para mostrar el listado de servicios.

    Obtiene todos los servicios existentes y los muestra en la plantilla.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        servicios = Servicio.objects.all()
        return render(request, 'servicios/listado.html', {'servicios': servicios})
    else:
        return redirect('/administracion/login')
