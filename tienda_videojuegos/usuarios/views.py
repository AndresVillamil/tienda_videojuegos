from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages

# Create your views here.

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Error en el inicio de sesión. Por favor, verifica tus credenciales.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')

@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')