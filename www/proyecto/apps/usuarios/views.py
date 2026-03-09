from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .models import Cliente

# Create your views here.

def usuarios_views(request):
    # Listado de clientes

    clientes = Cliente.objects.all()
    datos = {
        'parrafo':'Listado de Clientes',
        'clientes':clientes
    }
    return render(request, 'usuarios/index.html', datos)

def usuarios_alta_views(request):
    # Alta de nuevos clientes

    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        
        # Crear cliente en BD
        Cliente.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion
        )

        return redirect('usuarios_url')
       
    return render(request, 'usuarios/alta.html')

def usuarios_modificar_views(request):

    # Modificar (en desarrollo)
    return render(request, 'usuarios/modificar.html')

