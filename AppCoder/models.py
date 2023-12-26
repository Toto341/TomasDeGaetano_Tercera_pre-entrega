from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()


class Productos(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=6,decimal_places=6)
    Stock = models.IntegerField()

class Marcas(models.Model):
    nombre = models.CharField(max_length=30)
