from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    direccion = models.CharField(max_length=60)
    provincia = models.CharField(max_length=25)
    cp = models.IntegerField()
    dni = models.IntegerField()

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=30)
    cuit = models.IntegerField()
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=25)
    descuento = models.IntegerField()
    web = models.URLField()

class Producto(models.Model):
    nombre = models.CharField(max_length=35)
    variedad = models.CharField(max_length=20)
    contenido_ml = models.IntegerField()
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=150)

class Patrocinador(models.Model):
    nombre= models.CharField(max_length=15)
    rubro = models.CharField(max_length=30)
    slogan = models.CharField(max_length=100)
    antiguedad_anios = models.IntegerField()
    web = models.URLField()