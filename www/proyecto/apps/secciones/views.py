from django.shortcuts import render, redirect
from .models import Seccion

# Create your views here.
def secciones_views(request):
    """Vista para listar todas las secciones"""
    # Aquí luego recuperaremos las secciones de la BD: secciones = Seccion.objects.all()

    secciones = Seccion.objects.all()
    datos = {
        'parrafo': 'Listado de secciones disponibles en el sistema',
        'secciones': secciones 
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

