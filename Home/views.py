from django.shortcuts import render
from django.http import HttpResponse

def ejemplo(request):
    return HttpResponse("Hola, esta es la vista de ejemplo del Muro.")
