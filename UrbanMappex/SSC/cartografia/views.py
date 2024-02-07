from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user, force=True)  # Permite múltiples usuarios activos
            return redirect('home')  # Redirige a la página después del inicio de sesión exitoso
        else:
            error_message = "Credenciales inválidas"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def reset_session(request):
    # Actualiza la sesión
    request.session.modified = True
    return JsonResponse({'status': 'Session reset'})

def home(request):
    return render(request,'home.html')


def geosis(request):
    return render(request,'geoMap.html')


