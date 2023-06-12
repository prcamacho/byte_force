from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Cliente
from .forms import FormCliente, EditarFormCliente,AuthCliente
from .backend import BackEndCliente
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def nuevo_cliente(request):
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
            messages.success(request, "Cliente creado con éxito")
            return HttpResponseRedirect("/clientes/listado")       
    else:
        form=FormCliente()
    
    return render(request,'clientes/nuevo.html',{'form':form})

def desactivar_cliente(request,id):
    cliente_a_desactivar=get_object_or_404(Cliente,id=id)
    cliente_a_desactivar.activo=False
    cliente_a_desactivar.save()
    return redirect(reverse('clientes:listado_clientes'))

def activar_cliente(request,id):
    cliente_a_desactivar=get_object_or_404(Cliente,id=id)
    cliente_a_desactivar.activo=True
    cliente_a_desactivar.save()
    return redirect(reverse('clientes:listado_clientes'))

def listado_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'clientes/listado.html',{'clientes':clientes})


def modificar_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        formulario = EditarFormCliente(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/clientes/listado")
    else:
        formulario = EditarFormCliente(instance=cliente)
    return render(request, 'clientes/nuevo.html', {'form': formulario}) 


def log_in(request):
    esta=request.user.is_authenticated
    print(esta)
    if esta:
        redirect ("/home")
    else:    
        if request.method=='POST':
            form=AuthCliente(request.POST)
            if form.is_valid():
                dni=form.cleaned_data.get('dni')
                cliente=BackEndCliente().authenticate(request,dni=dni)
                print(cliente)
                if cliente is not None:
                    login(request,cliente,backend='clientes.backend.BackEndCliente')
                    redirect("/clientes/login") 
                else:
                    messages.error(request,'Cliente no encontrado')
            else:
                messages.error(request,'Usuario o contraseña no válido')        
        form=AuthCliente()
        return render(request,'usuario/cliente/nuevo.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect("/clientes/login") 