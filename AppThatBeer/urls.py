from django.urls import path
from AppThatBeer.models import Patrocinador
from AppThatBeer.views import aboutus, agregarCliente, agregarDistribuidor, agregarPatrocinador, agregarProducto, clientes, distribuidores, noticias, productos, patrocinadores, inicio, aboutus, noticias

urlpatterns = [
    path('', inicio, name= 'AppThatBeerInicio'),
    path('clientes/', clientes, name= 'AppThatBeerClientes'),
    path('distribuidores/', distribuidores, name= 'AppThatBeerDistribuidores'),
    path('patrocinadores/', patrocinadores, name= 'AppThatBeerPatrocinadores'),
    path('productos/', productos, name= 'AppThatBeerProductos'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),
    path('noticias/', noticias, name= 'AppThatBeerNoticias'),
    path('agregarcliente/', agregarCliente, name= 'AppThatBeerAgregarCliente'),
    path('agregardistribuidor/', agregarDistribuidor, name= 'AppThatBeerAgregarDistribuidor'),
    path('agregarpatrocinador/', agregarPatrocinador, name= 'AppThatBeerAgregarPatrocinador'),
    path('agregarproducto/', agregarProducto, name= 'AppThatBeerAgregarProducto'),
    

]