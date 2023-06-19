from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from clientes.models import Cliente
from .forms import *
from .backend import BackEndCliente
from django.contrib.auth import login,logout
from reservas.models import Reserva
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def registrar_cliente(request):
    """
    Vista para registrar un nuevo cliente.

    Si el usuario ya está autenticado, se redirige a la página de menú.
    Si se envía el formulario de registro y es válido, se crea el cliente y se inicia sesión.
    Luego, se redirige a la página de inicio.

    """
    if request.user.is_authenticated and request.user.empleado == False:
        return redirect('/menu/')
    
    form = FormCliente()
    
    if request.method == 'POST':
        form = FormCliente(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cliente_reg = Cliente.objects.create(
                nombre=cd['nombre'],
                apellido=cd['apellido'],
                dni=cd['dni'],
                email=cd['email']
            )
            
            cliente = BackEndCliente().authenticate(request, dni=cliente_reg.dni)
            
            if cliente is not None and cliente_reg.empleado == False:
                login(request, cliente, backend='menu_cliente.backend.BackEndCliente')
                return HttpResponseRedirect("/home/")
    
    return render(request, 'usuario/cliente/registro.html', {'form': form})


def modificar_cliente(request):
    """
    Vista para modificar los datos de un cliente existente.

    Se obtiene el cliente a través de su ID.
    Si se envía el formulario de modificación y es válido, se guardan los cambios.
    Luego, se redirige a la página de listado de clientes.

    """
    if request.user.is_authenticated and request.user.empleado == False:
        
        cliente = request.user
        
        if request.method == 'POST':
            form = EditarFormCliente(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/menu/")
        else:
            form = EditarFormCliente(instance=cliente)
        return render(request, 'usuario/cliente/actualizar_datos.html', {'form': form})
    else:
        return redirect('/menu/login/')


def log_in(request):
    """
    Vista para el inicio de sesión de un cliente.

    Si el usuario ya está autenticado, se redirige a la página de menú.
    Si se envía el formulario de inicio de sesión y es válido, se verifica el DNI del cliente.
    Si el cliente existe, se inicia sesión y se redirige a la página de menú.
    Si el DNI no está registrado, se muestra un mensaje de error.
    Si el formulario no es válido, se muestra un mensaje de error.

    """
    if request.user.is_authenticated and request.user.empleado == False:
        return redirect("/menu/")
    
    else:
        if request.method == 'POST':
            form = AuthCliente(request.POST)
            
            if form.is_valid():
                dni = form.cleaned_data.get('dni')
                cliente = BackEndCliente().authenticate(request, dni=dni)
                
                if cliente is not None:
                    login(request,cliente,backend='menu_cliente.backend.BackEndCliente')
                    return redirect("/menu/") 
                else:
                    messages.error(request,'DNI no registrado o no válido por favor Registrese')
            else:
                messages.error(request,'DNI no válido')        
        form=AuthCliente()
        return render(request,'usuario/cliente/login.html',{'form':form})


def log_out(request):
    """
    Vista para cerrar la sesión de un cliente.

    Se cierra la sesión y se redirige a la página de inicio.

    """
    logout(request)
    return redirect("/home/")


def reservas_user_cliente(request):
    """
    Vista para mostrar las reservas de un cliente.

    Si el usuario está autenticado, se obtienen las reservas del cliente y se muestran en la página de menú.
    Si el usuario no está autenticado, se redirige a la página de inicio.

    """
    if request.user.is_authenticated and request.user.empleado == False:
        reservas = Reserva.objects.filter(cliente=request.user,activo=True)
        return render(request, 'usuario/cliente/menu.html', {'reservas': reservas})
    
    else:
        return redirect('/menu/login/')
    
def desactivar_reserva(request,pk):
    reserva=get_object_or_404(Reserva,id=pk)
    reserva.activo=False
    reserva.save()
    return redirect ("/menu/")    

def modificar_reserva_user(request,id):
    reserva = get_object_or_404(Reserva, id=id,cliente=request.user)
    if request.method == 'POST':
        formulario = FormReserva(request.POST, instance=reserva)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/menu/")
    else:
        formulario = FormReserva(instance=reserva)
    return render(request, 'usuario/cliente/reserva.html', {'form': formulario}) 
    
def hacer_reserva(request):
    form=FormReserva()
    if request.method=='POST':
        form=FormReserva(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            reserva=Reserva.objects.create(fecha_reserva=cd['fecha_reserva'],
                                           cliente=request.user,
                                           responsable=cd['responsable'],
                                           empleado=cd['empleado'],
                                           servicio=cd['servicio'],
                                           precio=0
                                           )
            reserva.precio=reserva.servicio.precio
            reserva.save()
            email=request.user.email
            nombre_apellido=request.user.nombre +" "+request.user.apellido
            asunto="Reserva registrada con éxito!!!"
            from_email=settings.EMAIL_HOST_USER
            to=email
            template=render_to_string('email/reserva.html',{
                'nombre':nombre_apellido,
                'fecha_reserva':cd['fecha_reserva'],
                'responsable':cd['responsable'],
                'empleado':cd['empleado'],
                'servicio':cd['servicio'],
                'precio':reserva.precio
            })
            mensaje=strip_tags(template)
            send_mail(asunto,mensaje,from_email,[to],html_message=template)
            return HttpResponseRedirect("/menu/")       
    else:
        form=FormReserva()
    return render(request,'usuario/cliente/reserva.html',{'form':form})    