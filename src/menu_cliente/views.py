from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from clientes.models import Cliente
from .forms import FormCliente, EditarFormCliente, AuthCliente
from .backend import BackEndCliente
from django.contrib.auth import login, logout, authenticate
from reservas.models import Reserva

# Create your views here.
def registrar_cliente(request):
    """
    Vista para registrar un nuevo cliente.

    Si el usuario ya está autenticado, se redirige a la página de menú.
    Si se envía el formulario de registro y es válido, se crea el cliente y se inicia sesión.
    Luego, se redirige a la página de inicio.

    """
    if request.user.is_authenticated:
        return redirect('/menu')
    
    form = FormCliente()
    
    if request.method == 'POST':
        form = FormCliente(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cliente = Cliente.objects.create(
                nombre=cd['nombre'],
                apellido=cd['apellido'],
                dni=cd['dni'],
                email=cd['email']
            )
            
            cliente = BackEndCliente().authenticate(request, dni=cliente.dni)
            
            if cliente is not None:
                login(request, cliente, backend='clientes.backend.BackEndCliente')
                return HttpResponseRedirect("/home")
    
    return render(request, 'usuario/cliente/registro.html', {'form': form})


def modificar_cliente(request, id):
    """
    Vista para modificar los datos de un cliente existente.

    Se obtiene el cliente a través de su ID.
    Si se envía el formulario de modificación y es válido, se guardan los cambios.
    Luego, se redirige a la página de listado de clientes.

    """
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        form = EditarFormCliente(request.POST, instance=cliente)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/clientes/listado")
    
    else:
        form = EditarFormCliente(instance=cliente)
    
    return render(request, 'usuario/cliente/actualizar_datos.html', {'form': form})


def log_in(request):
    """
    Vista para el inicio de sesión de un cliente.

    Si el usuario ya está autenticado, se redirige a la página de menú.
    Si se envía el formulario de inicio de sesión y es válido, se verifica el DNI del cliente.
    Si el cliente existe, se inicia sesión y se redirige a la página de menú.
    Si el DNI no está registrado, se muestra un mensaje de error.
    Si el formulario no es válido, se muestra un mensaje de error.

    """
    if request.user.is_authenticated:
        return redirect("/menu")
    
    else:
        if request.method == 'POST':
            form = AuthCliente(request.POST)
            
            if form.is_valid():
                dni = form.cleaned_data.get('dni')
                cliente = BackEndCliente().authenticate(request, dni=dni)
                
                if cliente is not None:
                    login(request, cliente, backend='clientes.backend.BackEndCliente')
                    return redirect("/menu")
                
                else:
                    messages.error(request, 'DNI no registrado, por favor Registrese')
            
            else:
                messages.error(request, 'Usuario o contraseña no válido')
        
        form = AuthCliente()
        return render(request, 'usuario/cliente/registro.html', {'form': form})


def log_out(request):
    """
    Vista para cerrar la sesión de un cliente.

    Se cierra la sesión y se redirige a la página de inicio.

    """
    logout(request)
    return redirect("/home")


def reservas_user_cliente(request):
    """
    Vista para mostrar las reservas de un cliente.

    Si el usuario está autenticado, se obtienen las reservas del cliente y se muestran en la página de menú.
    Si el usuario no está autenticado, se redirige a la página de inicio.

    """
    if request.user.is_authenticated:
        reservas = Reserva.objects.filter(cliente=request.user)
        return render(request, 'usuario/cliente/menu.html', {'reservas': reservas})
    
    else:
        return redirect('/menu/login')
