from django.shortcuts import render

def vista_inicio(request):
    return render(request,'home/home.html')

def error_404(request, exception):
    return render(request,"404/404.html")

def error_400(request, exception):
    return render(request, "404/404.html", status=400)

