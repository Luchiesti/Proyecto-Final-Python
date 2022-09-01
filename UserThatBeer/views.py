from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


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
        'form': AuthenticationForm()
    }
    return render(request, 'UserThatBeer/login.html', contexto)
