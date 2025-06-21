from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido al manejo de geriatricos")


def ejemplo(request):
    return render(request, 'Home/Muro.html')

def identity_view(request):
    return render(request, 'Home/Identidad.html')

def services_view(request):
    return render(request, 'Home/servicios_generales.html')

def otros_view(request):
    return render(request, 'Home/Otroservicios.html')

def Contacto_view(request):
    return render(request, 'Home/Contacto.html')


def Login_view(request):
    return render(request, 'Home/Login.html')


from django.shortcuts import render
from django.http import JsonResponse
import json

def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = data.get('usuario')
            contrasena = data.get('contrasena')
            print("Usuario:", usuario)
            print("Contraseña:", contrasena)
            return JsonResponse({'mensaje': f'Usuario recibido: {usuario}'})
        except Exception as e:
            return JsonResponse({'error': 'Datos inválidos', 'detalles': str(e)}, status=400)

    return render(request, 'home/login.html')