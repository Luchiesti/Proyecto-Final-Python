from django.urls import path
from AppThatBeer.models import Patrocinador
from AppThatBeer.views import aboutus, crearCliente, crearDistribuidor, crearPatrocinador, crearProducto, clientes, \
    distribuidores, noticias, productos, patrocinadores, inicio, aboutus, noticias, buscarProducto, buscar, \
    leerProducto, eliminarProducto, editarProducto

urlpatterns = [
    # url generales
    path('', inicio, name= 'AppThatBeerInicio'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),
    path('noticias/', noticias, name= 'AppThatBeerNoticias'),
    path('buscar/', buscar, name='AppThatBeerBuscar'),

    # url productos
    path('productos/', leerProducto, name='AppThatBeerLeerProductos'),
    path('productos/crear', crearProducto, name='AppThatBeerCrearProducto'),
    path('productos/buscar', buscarProducto, name='AppThatBeerBuscarProducto'),
    path('productos/eliminar/<str:codigo>', eliminarProducto, name='AppThatBeerEliminarProducto'),
    path('productos/editar/<str:codigo>', editarProducto, name='AppThatBeerEditarProducto'),

    # url distribuidores
    path('distribuidores/', distribuidores, name='AppThatBeerDistribuidores'),
    path('distribuidores/crear', crearDistribuidor, name='AppThatBeerCrearDistribuidor'),

    # url patrocinadores
    path('patrocinadores/', patrocinadores, name='AppThatBeerPatrocinadores'),
    path('patrocinadores/crear', crearPatrocinador, name='AppThatBeerCrearPatrocinador'),

    # url clientes
    path('clientes/', clientes, name='AppThatBeerClientes'),
    path('clientes/crear', crearCliente, name='AppThatBeerCrearCliente'),

]