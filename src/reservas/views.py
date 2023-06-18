from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from django.contrib import messages
from .models import Reserva
# Create your views here.

def nueva_reserva(request):
    if request.user.is_authenticated and request.user.empleado == True:
        form=FormReserva()
        if request.method=='POST':
            form=FormReserva(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                Reserva.objects.create(fecha_reserva=cd['fecha_reserva'],
                                            cliente=cd['cliente'],
                                            responsable=cd['responsable'],
                                            empleado=cd['empleado'],
                                            servicio=cd['servicio'],
                                            precio=cd['precio']
                                            )
                return HttpResponseRedirect("/administracion/reservas/listado")       
        else:
            form=FormReserva()
        
        return render(request,'reservas/nuevo.html',{'form':form})
    else:
        return redirect('/administracion/login')

def listado_reservas(request):
    if request.user.is_authenticated and request.user.empleado == True:
        reservas=Reserva.objects.all()
        return render(request,'reservas/listado.html',{'reservas':reservas})
    else:
        return redirect('/administracion/login')

def modificar_reserva(request,id):
    if request.user.is_authenticated and request.user.empleado == True:
        reserva = get_object_or_404(Reserva, id=id)
        if request.method == 'POST':
            formulario = EditarFormReserva(request.POST, instance=reserva)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/administracion/reservas/listado")
        else:
            formulario = EditarFormReserva(instance=reserva)
            return render(request, 'reservas/nuevo.html', {'form': formulario}) 
    else:
        return redirect('/administracion/login')
    
def eliminar_reserva(request,id):
    if request.user.is_authenticated and request.user.empleado == True:
        reserva = get_object_or_404(Reserva, id=id)
        reserva.delete()
        return redirect('reservas:listado_reservas')
    else:
        return redirect('/administracion/login')
