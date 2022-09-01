from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppThatBeer.models import Cliente, Producto, Distribuidor, Patrocinador
from AppThatBeer.forms import ProductoFormulario, ClienteFormulario, DistribuidorFormulario, PatrocinadorFormulario


def clientes(request):
    return render(request, 'AppThatBeer/cliente/clientes.html')

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
    return render(request, 'AppThatBeer/distribuidor/distribuidores.html', contexto)


def productos(request):
    productoslistado = Producto.objects.all()
    return render(request, 'AppThatBeer/producto/productos.html', {"productos": productoslistado})


def inicio(request):
    return render(request, 'index.html')


def patrocinadores(request):
    return render(request, 'AppThatBeer/patrocinador/patrocinadores.html')


def aboutus(request):
    return render(request, 'AppThatBeer/aboutus/aboutus.html')


def noticias(request):
    return render(request, 'AppThatBeer/noticias/noticias.html')

@login_required
def crearCliente(request):
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

            return render(request, 'AppThatBeer/cliente/clientes.html')
    else:
        mi_formulario = ClienteFormulario()
    return render(request, 'AppThatBeer/cliente/crear.html', {'mi_formulario':mi_formulario})


def crearDistribuidor(request):
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

            return render(request, 'AppThatBeer/distribuidor/distribuidores.html')
    else:
        mi_formulario = DistribuidorFormulario()
    return render(request, 'AppThatBeer/distribuidor/crear.html', {'mi_formulario':mi_formulario})


def crearPatrocinador(request):
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

            return render(request, 'AppThatBeer/patrocinador/patrocinadores.html')
    else:
        mi_formulario = PatrocinadorFormulario()
    return render(request, 'AppThatBeer/patrocinador/crear.html', {'mi_formulario':mi_formulario})

def buscarProducto(request):
    return render(request, 'AppThatBeer/producto/buscar.html')

def buscar(request):
    if request.GET['variedad']:
        variedad = request.GET['variedad']
        productos = Producto.objects.filter(variedad__contains=variedad)

        return render(request, 'AppThatBeer/producto/resultadobusqueda.html', {'productos': productos, 'variedad': variedad})
    else:
        respuesta = 'No enviaste datos'
    return HttpResponse(respuesta)

def leerProducto(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'AppThatBeer/producto/leer.html', contexto)

def crearProducto(request):
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

            producto = Producto(nombre=nombre, variedad=variedad, contenido_ml=contenido_ml, codigo=codigo,
                                descripcion=descripcion)
            producto.save()

            return redirect('AppThatBeerLeerProductos')
        else:
            return redirect('AppThatBeerInicio')
    contexto = {
        'producto_form': ProductoFormulario()
    }
    return render(request, 'AppThatBeer/producto/crear.html', contexto)

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect('AppThatBeerLeerProductos')

def editarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto_form = ProductoFormulario(initial={
        'nombre':producto.nombre,
        'variedad':producto.variedad,
        'contenido_ml':producto.contenido_ml,
        'codigo':producto.codigo,
        'descripcion':producto.descripcion,
    })

    if request.method == 'POST':
        mi_form = ProductoFormulario(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            producto.nombre = info['nombre']
            producto.variedad = info['variedad']
            producto.contenido_ml = info['contenido_ml']
            producto.codigo = info['codigo']
            producto.descripcion = info['descripcion']

            producto.save()
            return redirect('AppThatBeerLeerProductos')
    contexto = {
        'producto_form': producto_form,
    }
    return render(request, 'AppThatBeer/producto/editar.html', contexto)