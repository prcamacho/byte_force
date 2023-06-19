from django.shortcuts import render
from django.http import HttpResponse

def vista_inicio(request):
    return render(request,'home/home.html')

def error_404(request, exception):
    return render(request,"404/404.html")

def error_400(request, exception):
    return render(request, "404/404.html", status=400)

def validacion_ssl(request):
    response = HttpResponse(content_type='text/plain')  
    response['Content-Disposition'] = 'inline; filename="B0E0FB918FD927D6E4611AEADAE89355.txt"'

    response.write('79EF7B2F2A6535E4CE94D11A3C72E572C5600DEF514110A513E5856F69AA36E0\ncomodoca.com\nea9d432eef8e078')

    return response

def invitados(request):
    return render(request, 'reservas/invitados.html')