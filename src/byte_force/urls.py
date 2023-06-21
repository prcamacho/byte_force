"""
URL configuration for byte_force project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import vista_inicio,validacion_ssl,invitados
#Capturar error 404
from django.conf.urls import handler404,handler400,handler500,handler403
from.views import error_404, error_400, error_500, error_403
urlpatterns = [
    path('.well-known/pki-validation/B0E0FB918FD927D6E4611AEADAE89355.txt',view=validacion_ssl,name='validacion ssl'),
    path('eventos/nL87kM/',invitados,name='invitados'),
    path('',view=vista_inicio, name='vista_inicio'),
    path('home/',view=vista_inicio, name='vista_inicio'),
    path('admin/', admin.site.urls),
    path('administracion/empleados/', include('empleados.urls', namespace='empleados')),
    path('administracion/clientes/',include('clientes.urls',namespace='clientes')),
    path('administracion/coordinadores/', include('coordinadores.urls',namespace='coordinadores')),
    path('administracion/reservas/',include('reservas.urls',namespace='reservas')),
    path('administracion/servicios/',include('servicios.urls',namespace='servicios')),
    path('api/',include('api.urls',namespace='api')),
    path('menu/',include('menu_cliente.urls')),
    path('administracion/',include('menu_empleado.urls')),
    
]

handler404 = error_404
handler400 = error_400
handler500 = error_500
handler403 = error_403