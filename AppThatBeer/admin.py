from django.contrib import admin

from AppThatBeer.models import Cliente, Producto, Patrocinador, Distribuidor

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Patrocinador)
admin.site.register(Distribuidor)
