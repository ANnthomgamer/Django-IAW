from django.db import models

class Proveedor(models.Model):
    """Modelo para proveedores"""
    nombre = models.CharField(max_length=100, unique=True)
    cif = models.CharField(max_length=20, unique=True, verbose_name="CIF/NIF")
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    web = models.URLField(blank=True, null=True, verbose_name="Sitio web")
    contacto = models.CharField(max_length=100, blank=True, null=True, verbose_name="Persona de contacto")
    notas = models.TextField(blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']
