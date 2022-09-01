from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserThatBeer.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = data.get('username')
            password = data.get('password')
            user = authenticate(username=user, password=password)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')
                return redirect('AppThatBeerInicio')

        else:
            messages.info(request, 'Inicio de sesion fallido!')
            return redirect('AppThatBeerInicio')

    contexto = {
        'form': AuthenticationForm(),
        'title': 'INICIO DE SESIÓN',
        'name_submit': 'Iniciar sesion',
    }
    return render(request, 'UserThatBeer/login.html', contexto)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado')
        return redirect('AppThatBeerInicio')

    contexto = {
        'form': UserRegisterForm(),
        'title': 'NUEVO REGISTRO',
        'name_submit': 'Registrarse',
    }
    return render(request, 'UserThatBeer/login.html', contexto)

