"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Muro/', views.ejemplo, name='Muro'),
    path('Identity/', views.identity_view, name='identity'),
    path('Services/', views.services_view, name='services'), 
    path('Otros/', views.otros_view, name='otros'), 
    path('Contacto/', views.contacto_view, name='Contacto'), 
    path('Login/', views.login_view, name='Login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
]



