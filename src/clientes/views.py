from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Cliente
from .forms import FormCliente, EditarFormCliente
import time

def nuevo_cliente(request):
    """
    Crea un nuevo cliente con los datos proporcionados en el formulario.
    Redirige al listado de clientes después de crear el cliente.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        form=FormCliente()
        if request.method=='POST':
            form=FormCliente(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                Cliente.objects.create(nombre=cd['nombre'],
                                        apellido=cd['apellido'],
                                        dni=cd['dni'],
                                        email=cd['email']
                                        )
                time.sleep(1.5)
                return HttpResponseRedirect("/administracion/clientes/listado/")       
        else:
            form=FormCliente()
            return render(request,'clientes/nuevo.html',{'form':form})
    else:
        return redirect('/administracion/login/')        
    

def desactivar_cliente(request,id):
    """
    Desactiva un cliente existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del cliente a desactivar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """    
    if request.user.is_authenticated and request.user.empleado == True:
        cliente_a_desactivar=get_object_or_404(Cliente,id=id)
        cliente_a_desactivar.activo=False
        cliente_a_desactivar.save()
        return redirect(reverse('clientes:listado_clientes'))
    else:
        return redirect('/administracion/login/')

def activar_cliente(request,id):
    if request.user.is_authenticated and request.user.empleado == True:   
        cliente_a_desactivar=get_object_or_404(Cliente,id=id)
        cliente_a_desactivar.activo=True
        cliente_a_desactivar.save()
        return redirect(reverse('clientes:listado_clientes'))
    else:
        return redirect('/administracion/login/')

def listado_clientes(request):
    """
    Activa un cliente existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del cliente a activar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    if request.user.is_authenticated and request.user.empleado == True:    
        clientes=Cliente.objects.all()
        return render(request,'clientes/listado.html',{'clientes':clientes})
    else:
        return redirect('/administracion/login/')

def modificar_cliente(request, id):
    """
    Modifica un cliente existente con los datos proporcionados en el formulario.
    Redirige al listado de clientes después de modificar el cliente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del cliente a modificar.
    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    if request.user.is_authenticated and request.user.empleado == True:
        cliente = get_object_or_404(Cliente, id=id)
        if request.method == 'POST':
            formulario = EditarFormCliente(request.POST, instance=cliente)
            if formulario.is_valid():
                formulario.save()
                time.sleep(1.5)
                return HttpResponseRedirect("/administracion/clientes/listado/")
        else:
            formulario = EditarFormCliente(instance=cliente)
        return render(request, 'clientes/nuevo.html', {'form': formulario}) 
    else:
        return redirect('/administracion/login/')