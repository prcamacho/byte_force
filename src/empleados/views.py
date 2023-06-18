from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .formulario import FormEmpleado, EditarFormularioEmpleado
from .models import Empleado
from django.contrib import messages
from django.forms import ModelForm


# Create your views here.

def nuevo_empleado(request):
    if request.user.is_authenticated and request.user.empleado == True:
        if request.method == "POST":
            
            formulario = FormEmpleado(request.POST)
            
            if formulario.is_valid():
                cd = formulario.cleaned_data
                
                Empleado.objects.create(nombre = cd['nombre'],
                                        apellido = cd['apellido'],
                                        email=cd['email'],
                                        dni=cd['dni'],                 
                                        numero_legajo = cd ['numero_legajo'])
                return HttpResponseRedirect ("/administracion/empleados/listado")
        else:
            formulario = FormEmpleado()
        return render(request, 'empleados/nuevo.html',{"form":formulario})
    else:
        return redirect('/administracion/login')
    
def modificar_empleado (request, id):
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = get_object_or_404(Empleado, id=id)
        if request.method == 'POST':
            formulario = EditarFormularioEmpleado(request.POST, instance=empleado)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/administracion/empleados/listado")
        else:
            formulario = EditarFormularioEmpleado(instance=empleado)
            return render(request, 'empleados/nuevo.html', {'form': formulario})
    else:
        return redirect('/administracion/login')     
    
def activar_empleado(request, id):
    if request.user.is_authenticated and request.user.empleado == True:
        empleado = get_object_or_404(Empleado, id=id)
        if empleado.activo == False:
            empleado.activo=True
            empleado.save()
        return HttpResponseRedirect ("/administracion/empleados/listado")
    else:
        return redirect('/administracion/login')

def desactivar_empleado(request,pk):
    if request.user.is_authenticated and request.user.empleado == True:
        empleado=get_object_or_404(Empleado,id=pk)
        empleado.activo=False
        empleado.save()
        return HttpResponseRedirect ("/administracion/empleados/listado")
    else:
        return redirect('/administracion/login')

def listado_empleados(request):
    if request.user.is_authenticated and request.user.empleado == True:
        empleados=Empleado.objects.all()
        return render(request,'empleados/listado.html',{'empleados':empleados})
    else:
        return redirect('/administracion/login')

    
