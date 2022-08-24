from django.urls import path
from AppThatBeer.models import Patrocinador
from AppThatBeer.views import aboutus, crearCliente, crearDistribuidor, crearPatrocinador, crearProducto, clientes, \
    distribuidores, noticias, productos, patrocinadores, inicio, aboutus, noticias, buscarProducto, buscar

urlpatterns = [
    path('', inicio, name= 'AppThatBeerInicio'),
    path('clientes/', clientes, name= 'AppThatBeerClientes'),
    path('distribuidores/', distribuidores, name= 'AppThatBeerDistribuidores'),
    path('patrocinadores/', patrocinadores, name= 'AppThatBeerPatrocinadores'),
    path('productos/', productos, name= 'AppThatBeerProductos'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),
    path('noticias/', noticias, name= 'AppThatBeerNoticias'),
    path('clientes/crear', crearCliente, name='AppThatBeerCrearCliente'),
    path('distribuidores/crear', crearDistribuidor, name='AppThatBeerCrearDistribuidor'),
    path('patrocinadores/crear', crearPatrocinador, name='AppThatBeerCrearPatrocinador'),
    path('productos/crear', crearProducto, name='AppThatBeerCrearProducto'),
    path('productos/buscar', buscarProducto, name='AppThatBeerBuscarProducto'),
    path('buscar/', buscar, name='AppThatBeerBuscar')
]