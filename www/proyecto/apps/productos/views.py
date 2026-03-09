from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .models import Producto # Importar el modelo
from apps.secciones.models import Seccion


# Create your views here.
 
def productos_views(request):
    """
    doc_externo = open("proyecto/templates/index.html")

    #mensaje = "Estas en la pantalla Productos"
    mensaje = "PRODUCTOS"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"parrafo":mensaje})
    
    documento = planti.render(ctx)
    """
    productos = Producto.objects.all()
    datos = {
        'parrafo': 'PRODUCTOS',
        'productos': productos  # Pasar a la plantilla
    }


    return render(request, "productos/index.html", datos)
    # return HttpResponse(documento)

def productos_alta_views(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
    
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
    else:
        secciones = Seccion.objects.all()
        return render(request, 'productos/alta.html', {'secciones': secciones})

    return redirect('productos_url')



def productos_modificar_views(request):
    return render(request, 'productos/modificar.html')


