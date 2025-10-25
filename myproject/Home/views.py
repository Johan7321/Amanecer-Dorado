from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from accounts.models import Organization

# -------------------------------
# REGISTRO (SIGNUP)
# -------------------------------
def signup(request):
    """
    Permite a un usuario crear una nueva cuenta y su propia organización (cliente SaaS).
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        org_name = request.POST.get('org_name')

        if form.is_valid() and org_name:
            user = form.save()
            slug = slugify(org_name)
            org = Organization.objects.create(name=org_name, slug=slug)

            profile = user.profile
            profile.organization = org
            profile.is_owner = True
            profile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


# -------------------------------
# DASHBOARD (ÁREA PRIVADA)
# -------------------------------
@login_required
def dashboard(request):
    """
    Vista principal del panel del usuario (dashboard).
    Muestra información de la organización asociada.
    """
    org = getattr(request.user.profile, "organization", None)
    return render(request, 'Home/dashboard.html', {'org': org})

def index(request):
    return HttpResponse("Bienvenido al manejo de geriátricos")