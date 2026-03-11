from django.db import models
from apps.secciones.models import Seccion
from apps.proveedores.models import Proveedor

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    # Relación con secciones (opcional)
    seccion = models.ForeignKey('secciones.Seccion', on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='productos'
    )



    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


