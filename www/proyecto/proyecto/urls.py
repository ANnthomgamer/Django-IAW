"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.inicio.views import saludo, easter_egg
from apps.ventas.views import ventas_views, ventas_alta_views, ventas_borrar_views
from apps.productos.views import productos_views, productos_alta_views, productos_modificar_views
from apps.secciones.views import secciones_views, secciones_alta_views, secciones_modificar_views
from apps.usuarios.views import usuarios_views, usuarios_alta_views, usuarios_modificar_views
from apps.config.views import config_views, config_modificar_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',saludo),
    
    path('productos/', productos_views, name='productos_url'),
    path('productos/alta', productos_alta_views, name='productos_alta'),
    path('productos/modificar', productos_modificar_views, name='productos_modificar'),
    
    path('secciones/', secciones_views, name='secciones_url'),
    path('secciones/alta', secciones_alta_views, name='secciones_alta'),
    path('secciones/modificar', secciones_modificar_views, name='secciones_modificar'),

    path('ventas/', ventas_views, name='ventas_url'),
    path('ventas/alta', ventas_alta_views, name='ventas_alta'),
    path('ventas/borrar', ventas_borrar_views, name='ventas_borrar'),

    path('usuarios/', usuarios_views, name='usuarios_url'),
    path('usuarios/alta', usuarios_alta_views, name='usuarios_alta'),
    path('usuarios/modificar', usuarios_modificar_views, name='usuarios_modificar'),

    path('easter_egg', easter_egg),

    path('config/', config_views, name='config_url'),
    path('config/modificar', config_modificar_views, name='config_modificar'),

]
