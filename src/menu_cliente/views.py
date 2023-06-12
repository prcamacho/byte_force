from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from clientes.models import Cliente
from .forms import FormCliente, EditarFormCliente,AuthCliente
from .backend import BackEndCliente
from django.contrib.auth import login,logout,authenticate
from reservas.models import Reserva

# Create your views here.
def registrar_cliente(request):
    if request.user.is_authenticated:
        return redirect('/menu')
    form=FormCliente()
    if request.method=='POST':
        form=FormCliente(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            cliente=Cliente.objects.create(nombre=cd['nombre'],
                                    apellido=cd['apellido'],
                                    dni=cd['dni'],
                                    email=cd['email']
                                    )
            cliente=BackEndCliente().authenticate(request,dni=cliente.dni)
            if cliente is not None:
                login(request,cliente,backend='clientes.backend.BackEndCliente')
                return HttpResponseRedirect("/home")       
    else:
        form=FormCliente()
    
    return render(request,'usuario/cliente/registro.html',{'form':form})


def modificar_cliente(request,id):
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
    if request.user.is_authenticated:
        return redirect ("/menu")
    else:    
        if request.method=='POST':
            form=AuthCliente(request.POST)
            if form.is_valid():
                dni=form.cleaned_data.get('dni')
                cliente=BackEndCliente().authenticate(request,dni=dni)
                if cliente is not None:
                    login(request,cliente,backend='clientes.backend.BackEndCliente')
                    return redirect("/menu") 
                else:
                    messages.error(request,'DNI no registrado, por favor Registrese')
            else:
                messages.error(request,'Usuario o contraseña no válido')        
        form=AuthCliente()
        return render(request,'usuario/cliente/registro.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect("/home") 

def reservas_user_cliente(request):
    if request.user.is_authenticated:
        reservas=Reserva.objects.filter(cliente=request.user)
        return render(request, 'usuario/cliente/menu.html',{'reservas':reservas})
    else:
        return redirect('/menu/login')