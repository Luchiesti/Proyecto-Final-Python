from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=60)
    provincia = forms.CharField(max_length=25)
    cp = forms.IntegerField()
    dni = forms.IntegerField()    

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=35)
    variedad = forms.CharField(max_length=20)
    contenido_ml = forms.IntegerField()
    codigo = forms.CharField(max_length=10)
    descripcion = forms.CharField(max_length=150)    

class DistribuidorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    cuit = forms.IntegerField()
    direccion = forms.CharField(max_length=45)
    provincia = forms.CharField(max_length=25)
    descuento = forms.IntegerField()
    web = forms.URLField()

class PatrocinadorFormulario(forms.Form):
    nombre= forms.CharField(max_length=15)
    rubro = forms.CharField(max_length=30)
    slogan = forms.CharField(max_length=100)
    antiguedad_anios = forms.IntegerField()
    web = forms.URLField()