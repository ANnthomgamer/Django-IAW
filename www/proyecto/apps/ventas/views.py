from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime, timedelta
from .models import Venta
from apps.usuarios.models import Cliente
from apps.productos.models import Producto


# Create your views here.

def ventas_views(request):
    """
    doc_externo = open("proyecto/templates/index.html")

    #mensaje = "Estas en la pantalla de Ventas"
    mensaje = "VENTAS"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"parrafo":mensaje})
    
    documento = planti.render(ctx)
    """
    
    # Fecha:
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    # Base del listado:
    ventas = Venta.objects.all().order_by('-fecha')

    # Aplicar filtros:

    if fecha_desde:
        ventas = ventas.filter(fecha__date__gte=fecha_desde)
    if fecha_hasta:
        ventas = ventas.filter(fecha__date__lte=fecha_hasta)

    # Datos a mostrar:
    datos = {
        'parrafo': 'LISTADO DE VENTAS',
        'ventas': ventas,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
    }

    return render(request, "ventas/index.html", datos)
    


def ventas_alta_views(request):
    """Alta de nuevas ventas"""

    if request.method == 'POST':
        # Generar código automático (podría mejorarse)
        ultima_venta = Venta.objects.all().order_by('-id').first()
        if ultima_venta:
            ultimo_numero = int(ultima_venta.codigo_venta.split('-')[-1])
            nuevo_numero = ultimo_numero + 1
        else:
            nuevo_numero = 1
        codigo = f"V-{nuevo_numero:04d}"
        
        # Recoger datos
        cliente_id = request.POST.get('cliente')
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        
        # Obtener producto y su precio
        producto = Producto.objects.get(id=producto_id)
        precio = producto.precio
        
        # Fecha
        fecha_str = request.POST.get('fecha')
        if fecha_str:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        else:
            fecha = timezone.now()

        # Crear venta
        venta = Venta(
            codigo_venta=codigo,
            cliente_id=cliente_id,
            producto_id=producto_id,
            precio_producto=precio,
            cantidad=cantidad,
        )
        
        venta.fecha = fecha
        venta.save()

        return redirect('ventas_url')
    
    # Si es GET, mostrar formulario con clientes y productos
    clientes = Cliente.objects.all().order_by('nombre')
    productos = Producto.objects.all().order_by('nombre')
    
    datos = {
        'clientes': clientes,
        'productos': productos,
    }
    return render(request, 'ventas/alta.html', datos)



# return HttpResponse(documento)
