from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def ventas_views(request):
    doc_externo = open("proyecto/templates/index.html")

    #mensaje = "Estas en la pantalla de Ventas"
    mensaje = "VENTAS"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"parrafo":mensaje})
    
    documento = planti.render(ctx)
    
    return render(request, "ventas/index.html", {"parrafo":mensaje})
    # return HttpResponse(documento)
