# En Mi_buscador/urls.py
from django.urls import path
from .views import buscar_palabra

urlpatterns = [
    path('buscar/', buscar_palabra, name='buscar'),
    # Otras rutas de tu aplicación...
]
