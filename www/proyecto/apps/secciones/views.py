from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Seccion

# Create your views here.
def secciones_views(request):
    """Vista para listar todas las secciones"""
    # Aquí luego recuperaremos las secciones de la BD: secciones = Seccion.objects.all()

    # Buscar termino:
    buscar = request.GET.get('buscar', '')

    # Base
    secciones = Seccion.objects.all()
    
    if buscar:
        secciones = secciones.filter(
            Q(nombre__icontains=buscar) |    # Buscar nombre sin key sensitive
            Q(descripcion__icontains=buscar) # Igual pero descripcion

        )

    # Ordenar por nombre
    secciones = secciones.order_by('nombre')

    datos = {
        'parrafo': 'Listado de secciones disponibles en el sistema',
        'secciones': secciones,
        'buscar':buscar,
    }
    return render(request, 'secciones/index.html', datos)

def secciones_alta_views(request):
    """Vista para el formulario de creación de secciones"""
    if request.method == 'POST':
        # Aquí irá la lógica para guardar en la BD
        # nombre = request.POST.get('nom_sec')
        # Seccion.objects.create(nom_sec=nombre)
        
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        Seccion.objects.create(
            nombre = nombre,
            descripcion = descripcion
        )

        return redirect('secciones_url') # Redirige al listado tras guardar
        
    datos = {
        'parrafo': 'Complete el formulario para dar de alta una nueva categoría.'
    }
    return render(request, 'secciones/alta.html', datos)

def secciones_modificar_views(request):
    """Modificar una sección existente"""
    
    # Obtener el ID de la sección
    seccion_id = request.GET.get('id') or request.POST.get('id')
    
    if not seccion_id:
        return redirect('secciones_url')
    
    # Obtener la sección
    seccion = get_object_or_404(Seccion, id=seccion_id)
    
    if request.method == 'POST':
        # Recoger datos
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        
        # Actualizar sección
        seccion.nombre = nombre
        seccion.descripcion = descripcion
        seccion.save()
        
        return redirect('secciones_url')
    
    # Si es GET, mostrar formulario con datos
    datos = {
        'seccion': seccion
    }

    return render(request, 'secciones/modificar.html', datos)
