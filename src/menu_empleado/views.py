from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .backend import *
from .forms import *
from django.contrib.auth import login,logout
from reservas.models import Reserva
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
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
                return redirect('/clientes/listado')
            else:
                messages.error(request,'Usuario o contraseña no válido')
        else:
            messages.error(request,'Usuario o contraseña no válido')        
    form=AuthEmpleado()
    return render(request,'login/login.html',{'form':form})