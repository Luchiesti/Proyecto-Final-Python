from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Avatar(models.Model):
    # referencia uno a uno
    # Al eliminar el usuario se elimina por 'cascada' el avatar
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
