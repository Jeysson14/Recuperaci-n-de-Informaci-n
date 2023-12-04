# En Mi_buscador/forms.py
from django import forms

class BusquedaForm(forms.Form):
    palabra = forms.CharField(label='Palabra a buscar', max_length=100)
