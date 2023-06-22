from django.shortcuts import render, redirect
from django.contrib import messages
from .backend import *
from .forms import *
from django.contrib.auth import login,logout
from reservas.models import Reserva
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
import time
# Create your views here.

def menu_administracion(request):
    return render(request,'home/home_empleado.html')

def log_in(request):
    if request.method=='POST':
        form=AuthEmpleado(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            empleado=BackEndEmpleado().authenticate(request,email=email,password=password)   
            if empleado is not None:
                login(request,empleado,backend='menu_empleado.backend.BackEndEmpleado')
                return redirect('/administracion/clientes/listado/')
            else:
                messages.error(request,'Usuario o contraseña no válido')
        else:
            messages.error(request,'Usuario o contraseña no válido')        
    form=AuthEmpleado()
    return render(request,'login/login.html',{'form':form})

def log_out(request):
    """
    Vista para cerrar la sesión de un cliente.

    Se cierra la sesión y se redirige a la página de inicio.

    """
    logout(request)
    return redirect("/administracion/login/")

def modificar_empleado(request):
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = request.user
        if request.method == 'POST':
            form = EditarEmpleado(request.POST, request.FILES, instance=empleado)
            if form.is_valid():
                form.save()
                time.sleep(1.5)
                return redirect("/administracion/")
        else:
            form = EditarEmpleado(instance=empleado)
        return render(request, 'usuario/empleado/modificar_empleado.html', {'form': form})
    else:
        return redirect('/administracion/login/') 