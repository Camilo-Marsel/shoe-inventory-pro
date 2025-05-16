from django.db import models
from django.contrib.auth.models import AbstractUser

# Opcional: Si deseas usuarios personalizados
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('staff', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

class Producto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.DecimalField(max_digits=4, decimal_places=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
