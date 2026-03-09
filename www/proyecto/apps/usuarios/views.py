from django.shortcuts import render, redirect, get_object_or_404
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

    # Modificar
    cliente_id = request.GET.get('id') or request.POST.get('id')
    
    if not cliente_id:
        return redirect('usuarios_url')
    
    # Obtener el cliente o mostrar 404 si no existe
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        
        # Actualizar cliente
        cliente.nombre = nombre
        cliente.email = email
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.save()
        
        return redirect('usuarios_url')  # Redirige al listado
    
    # Si es GET, mostrar formulario con datos del cliente
    datos = {
        'cliente': cliente
    }
    return render(request, 'usuarios/modificar.html', datos)
    



