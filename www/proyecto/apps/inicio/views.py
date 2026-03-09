from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    doc_externo = open("proyecto/templates/index.html")

    mensaje = "Estas en la pantalla de Inicio"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"parrafo":mensaje})
    
    documento = planti.render(ctx)
    
    return HttpResponse(documento)

