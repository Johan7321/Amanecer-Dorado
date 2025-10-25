from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.contrib import messages
from Home.models import Organization  # asegúrate de que este modelo exista


def signup(request):
    """Vista para registrar una nueva organización y usuario propietario"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        org_name = request.POST.get('org_name')

        if form.is_valid() and org_name:
            user = form.save()
            slug = slugify(org_name)
            org = Organization.objects.create(name=org_name, slug=slug)

            # Asumiendo que tienes un modelo Profile con un campo organization
            profile = user.profile
            profile.organization = org
            profile.is_owner = True
            profile.save()

            login(request, user)
            messages.success(request, "Registro completado exitosamente.")
            return redirect('dashboard')
        else:
            messages.error(request, "Error al registrar el usuario o la organización.")
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """Vista de inicio de sesión"""
    if request.method == 'POST':
        from django.contrib.auth import authenticate
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Credenciales inválidas.")
    return render(request, 'accounts/login.html')


def logout_view(request):
    """Cerrar sesión"""
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
