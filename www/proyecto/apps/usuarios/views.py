from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def usuarios_views(request):
    return render(request, 'usuarios/index.html')

def usuarios_alta_views(request):
    return render(request, 'usuarios/alta.html')

def usuarios_modificar_views(request):
    return render(request, 'usuarios/modificar.html')

