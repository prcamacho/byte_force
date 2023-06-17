from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Cliente
from .forms import FormCliente, EditarFormCliente

def nuevo_cliente(request):
    """
    Crea un nuevo cliente con los datos proporcionados en el formulario.
    Redirige al listado de clientes después de crear el cliente.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Cliente.objects.create(
                nombre=cd['nombre'],
                apellido=cd['apellido'],
                dni=cd['dni'],
                email=cd['email']
            )
            messages.success(request, "Cliente creado con éxito")
            return HttpResponseRedirect("/clientes/listado")
    else:
        form = FormCliente()
    
    return render(request, 'clientes/nuevo.html', {'form': form})

def desactivar_cliente(request, id):
    """
    Desactiva un cliente existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del cliente a desactivar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    cliente_a_desactivar = get_object_or_404(Cliente, id=id)
    cliente_a_desactivar.activo = False
    cliente_a_desactivar.save()
    return redirect(reverse('clientes:listado_clientes'))

def activar_cliente(request, id):
    """
    Activa un cliente existente.

    Parámetros:
    - request: La solicitud HTTP recibida.
    - id: El ID del cliente a activar.

    Devuelve:
    - Una respuesta HTTP redirigiendo al listado de clientes.
    """
    cliente_a_activar = get_object_or_404(Cliente, id=id)
    cliente_a_activar.activo = True
    cliente_a_activar.save()
    return redirect(reverse('clientes:listado_clientes'))

def listado_clientes(request):
    """
    Muestra el listado de clientes.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Devuelve:
    - Una respuesta HTTP renderizando el listado de clientes.
    """
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado.html', {'clientes': clientes})

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
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        formulario = EditarFormCliente(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/clientes/listado")
    else:
        formulario = EditarFormCliente(instance=cliente)
    return render(request, 'clientes/nuevo.html', {'form': formulario})
