from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Proveedor

def proveedores_views(request):
    """Listado de proveedores"""
    
    # Búsqueda
    buscar = request.GET.get('buscar', '')
    
    # Base
    proveedores = Proveedor.objects.all()
    
    if buscar:
        proveedores = proveedores.filter(
            Q(nombre__icontains=buscar) |
            Q(cif__icontains=buscar) |
            Q(email__icontains=buscar) |
            Q(contacto__icontains=buscar)
        )
    
    proveedores = proveedores.order_by('nombre')
    
    datos = {
        'parrafo': 'LISTADO DE PROVEEDORES',
        'proveedores': proveedores,
        'buscar': buscar,
    }
    return render(request, 'proveedores/index.html', datos)

def proveedores_alta_views(request):
    """Alta de nuevos proveedores"""
    
    if request.method == 'POST':
        # Recoger datos
        nombre = request.POST.get('nombre')
        cif = request.POST.get('cif')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        web = request.POST.get('web')
        contacto = request.POST.get('contacto')
        notas = request.POST.get('notas')
        
        # Crear proveedor
        Proveedor.objects.create(
            nombre=nombre,
            cif=cif,
            direccion=direccion,
            telefono=telefono,
            email=email,
            web=web,
            contacto=contacto,
            notas=notas
        )
        
        return redirect('proveedores_url')
    
    return render(request, 'proveedores/alta.html')

def proveedores_modificar_views(request):
    """Modificar un proveedor existente"""
    
    proveedor_id = request.GET.get('id') or request.POST.get('id')
    
    if not proveedor_id:
        return redirect('proveedores_url')
    
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.cif = request.POST.get('cif')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.web = request.POST.get('web')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.notas = request.POST.get('notas')
        proveedor.save()
        
        return redirect('proveedores_url')
    
    datos = {
        'proveedor': proveedor
    }
    return render(request, 'proveedores/modificar.html', datos)
