from django.urls import path
from . import views

urlpatterns = [
    path('Muro/', views.Muro, name='Muro'),
]
