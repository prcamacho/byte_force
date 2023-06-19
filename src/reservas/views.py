from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormReserva, EditarFormReserva
from django.contrib import messages
from .models import Reserva
from servicios.models import Servicio

# Create your views here.
def nueva_reserva(request):
    """
    Vista para crear una nueva reserva.

    Si se envía el formulario de reserva y es válido, se crea la reserva y se redirige al listado de reservas.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        if request.method=='POST':
            form=FormReserva(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                reserva=Reserva.objects.create(fecha_reserva=cd['fecha_reserva'],
                                            cliente=cd['cliente'],
                                            responsable=cd['responsable'],
                                            empleado=cd['empleado'],
                                            servicio=cd['servicio'],
                                            precio=0
                                            )
                reserva.precio=reserva.servicio.precio
                reserva.save()
                return HttpResponseRedirect("/administracion/reservas/listado")       
        else:
            form=FormReserva()
        return render(request,'reservas/nuevo.html',{'form':form})
    else:
        return redirect('/administracion/login')

def listado_reservas(request):
    if request.user.is_authenticated and request.user.empleado == True:
        """
    Vista para mostrar el listado de reservas.

    Se obtienen todas las reservas y se muestran en la página de listado de reservas.

    """
        reservas = Reserva.objects.all()
        return render(request, 'reservas/listado.html', {'reservas': reservas})
    else:
        return redirect('/administracion/login')


def modificar_reserva(request, id):
    """
    Vista para modificar una reserva existente.

    Se obtiene la reserva a través de su ID.
    Si se envía el formulario de modificación y es válido, se guardan los cambios.
    Luego, se redirige al listado de reservas.

    """
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


def eliminar_reserva(request, id):
    """
    Vista para eliminar una reserva.

    Se obtiene la reserva a través de su ID y se elimina.
    Luego, se redirige al listado de reservas.

    """
    if request.user.is_authenticated and request.user.empleado == True:
        reserva = get_object_or_404(Reserva, id=id)
        reserva.delete()
        return redirect('reservas:listado_reservas')
    else:
        return redirect('/administracion/login')
