from django.db import models
from apps.usuarios.models import Cliente
from apps.productos.models import Producto

# Create your models here.

class Venta(models.Model):
    codigo_venta = models.CharField(max_length=20, unique=True)  # CÓDIGO DE LA VENTA
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')  # CLIENTE
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')  # PRODUCTO
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)  # PRECIO (podría ser el del producto en ese momento)
    cantidad = models.PositiveIntegerField()  # CANTIDAD
    fecha = models.DateTimeField(auto_now_add=True)  # FECHA (automática al crear)
    
    @property
    def total(self):
        """Calcula el total de la venta"""
        return self.precio_producto * self.cantidad
    
    def __str__(self):
        return f"Venta {self.codigo_venta} - {self.cliente} - ${self.total}"
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha']  # Las más recientes primero
