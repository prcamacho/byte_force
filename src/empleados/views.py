from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .formulario import FormEmpleado, EditarFormularioEmpleado
from .models import Empleado
from django.contrib import messages
from django.forms import ModelForm


# Create your views here.

def nuevo_empleado(request):
    
    if request.method == "POST":
        
        formulario = FormEmpleado(request.POST)
        
        if formulario.is_valid():
            cd = formulario.cleaned_data
            
            Empleado.objects.create(nombre = cd['nombre'],
                                    apellido = cd['apellido'],
                                    email=cd['email'],
                                    dni=cd['dni'],                 
                                    numero_legajo = cd ['numero_legajo'])
            messages.success(request, "Empleado agregado con exito")
            return HttpResponseRedirect ("/empleados/listado")
        
    else:
        formulario = FormEmpleado()
    return render(request, 'empleados/nuevo.html',{"form":formulario})

def modificar_empleado (request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        formulario = EditarFormularioEmpleado(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/empleados/listado")
    else:
        formulario = EditarFormularioEmpleado(instance=empleado)
        return render(request, 'empleados/nuevo.html', {'form': formulario}) 
    
def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if empleado.activo == False:
        empleado.activo=True
        empleado.save()
        #messages.success(request, "Empleado activado con exito")
    #else:
        #messages.success(request, "Empleado ya esta activo")
    return HttpResponseRedirect ("/empleados/listado")

def desactivar_empleado(request,pk):
    empleado=get_object_or_404(Empleado,id=pk)
    empleado.activo=False
    empleado.save()
    return HttpResponseRedirect ("/empleados/listado")

def listado_empleados(request):
    empleados=Empleado.objects.all()
    return render(request,'empleados/listado.html',{'empleados':empleados})

    
