from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Template, Context
from .models import Producto
from apps.secciones.models import Seccion
from apps.proveedores.models import Proveedor
from django.db.models import Q

# Create your views here.

def productos_views(request):
    """
    Vista de listado de productos con búsqueda
    """
    buscar = request.GET.get('buscar', '')

    productos = Producto.objects.all()

    if buscar:
        productos = productos.filter(
            Q(nombre__icontains=buscar) |
            Q(descripcion__icontains=buscar)
        )

    datos = {
        'parrafo': 'PRODUCTOS',
        'productos': productos,
        'buscar': buscar
    }

    return render(request, "productos/index.html", datos)


def productos_alta_views(request):
    """
    Vista de alta de productos (ahora con proveedores)
    """
    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        seccion_id = request.POST.get('seccion')
        proveedor_id = request.POST.get('proveedor')  

        # Crear el producto
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        
        # Asignar sección si se seleccionó
        if seccion_id:
            producto.seccion_id = seccion_id
            
        # Asignar proveedor si se seleccionó
        if proveedor_id:
            producto.proveedor_id = proveedor_id
            
        # Guardar en BD
        producto.save()

        return redirect('productos_url')

    else:
        # Si es GET, mostrar formulario con listados
        secciones = Seccion.objects.all().order_by('nombre')
        proveedores = Proveedor.objects.all().order_by('nombre')
        return render(request, 'productos/alta.html', {
            'secciones': secciones,
            'proveedores': proveedores
        })


def productos_modificar_views(request):
    """
    Vista para modificar un producto existente
    """
    # Obtener el ID del producto
    producto_id = request.GET.get('id') or request.POST.get('id')

    if not producto_id:
        return redirect('productos_url')

    # Obtener el producto
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        seccion_id = request.POST.get('seccion')
        proveedor_id = request.POST.get('proveedor')  

        # Actualizar producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        
        # Actualizar sección
        if seccion_id:
            producto.seccion_id = seccion_id
        else:
            producto.seccion = None
            
        # Actualizar proveedor
        if proveedor_id:
            producto.proveedor_id = proveedor_id
        else:
            producto.proveedor = None
            
        producto.save()

        return redirect('productos_url')

    # Si es GET, mostrar formulario con datos
    secciones = Seccion.objects.all().order_by('nombre')
    proveedores = Proveedor.objects.all().order_by('nombre')  
    datos = {
        'producto': producto,
        'secciones': secciones,
        'proveedores': proveedores,  
    }

    return render(request, 'productos/modificar.html', datos)
