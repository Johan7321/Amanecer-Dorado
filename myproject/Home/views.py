from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido al manejo de geriatricos")


def ejemplo(request):
    return render(request, 'Home/Muro.html')

def identity_view(request):
    return render(request, 'Home/Identidad.html')