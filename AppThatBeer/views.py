from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppThatBeer.models import Cliente, Producto, Distribuidor, Patrocinador
from AppThatBeer.forms import ProductoFormulario, ClienteFormulario, DistribuidorFormulario, PatrocinadorFormulario


def clientes(request):

    return render(request, 'clientes.html')

def distribuidores(request):
    contexto = {
        'distribuidores': {
            'distribuidor1': 'Patagonia',
            'distribuidor2': 'Temple',
            'distribuidor3': 'Pentos',
            'distribuidor4': 'Pinta Point', 
            'distribuidor5': 'Prinston',
            'distribuidor6': 'Maldita Malta',
            'distribuidor7': 'Braavos Bar',

        }
    }
    return render(request, 'distribuidores.html', contexto)


def productos(request):
    productoslistado = Producto.objects.all()
    return render(request, 'productos.html', {"productos": productoslistado})


def inicio(request):
    return render(request, 'index.html')


def patrocinadores(request):
    return render(request, 'patrocinadores.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def noticias(request):
    return render(request, 'noticias.html')


def agregarCliente(request):
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            email = informacion['email']
            direccion = informacion['direccion']
            provincia = informacion['provincia']
            cp = informacion['cp']
            dni = informacion['dni']

            cliente = Cliente(nombre=nombre, apellido=apellido, email=email, direccion=direccion, provincia=provincia, cp=cp, dni=dni)
            cliente.save()

            return render(request, 'clientes.html')
    else:
        mi_formulario = ClienteFormulario()
    return render(request, 'agregarcliente.html', {'mi_formulario':mi_formulario})


def agregarDistribuidor(request):
    if request.method == 'POST':
        mi_formulario = DistribuidorFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            cuit = informacion['cuit']
            direccion = informacion['direccion']
            provincia = informacion['provincia']
            descuento = informacion['descuento']
            web = informacion['web']

            distribuidor = Distribuidor(nombre=nombre, cuit=cuit, direccion=direccion, provincia=provincia, descuento=descuento, web=web)
            distribuidor.save()

            return render(request, 'distribuidores.html')
    else:
        mi_formulario = DistribuidorFormulario()
    return render(request, 'agregardistribuidor.html', {'mi_formulario':mi_formulario})


def agregarPatrocinador(request):
    if request.method == 'POST':
        mi_formulario = PatrocinadorFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            rubro = informacion['rubro']
            slogan = informacion['slogan']
            antiguedad_anios = informacion['antiguedad_anios']
            web = informacion['web']

            patrocinador = Patrocinador(nombre=nombre, rubro=rubro, slogan=slogan, antiguedad_anios=antiguedad_anios, web=web)
            patrocinador.save()

            return render(request, 'patrocinadores.html')
    else:
        mi_formulario = PatrocinadorFormulario()
    return render(request, 'agregarpatrocinador.html', {'mi_formulario':mi_formulario})


def agregarProducto(request):
    if request.method == 'POST':
        mi_formulario = ProductoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            variedad = informacion['variedad']
            contenido_ml = informacion['contenido_ml']
            codigo = informacion['codigo']
            descripcion = informacion['descripcion']

            producto = Producto(nombre=nombre, variedad=variedad, contenido_ml=contenido_ml, codigo=codigo, descripcion=descripcion)
            producto.save()

            return render(request, 'productos.html')
    else:
        mi_formulario = ProductoFormulario()
    return render(request, 'agregarproducto.html', {'mi_formulario':mi_formulario})

