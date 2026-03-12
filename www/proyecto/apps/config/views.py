from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def config_views(request):
#     return HttpResponse('config/index.html')
    return render(request, 'config/index.html')

def config_modificar_views(request):
    return render(request, 'config/modificar.html')

