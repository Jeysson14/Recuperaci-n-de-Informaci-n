import os
from django.shortcuts import render
from .forms import BusquedaForm
import ast

def buscar_palabra(request):
    resultado = None

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            palabra = form.cleaned_data['palabra'].lower()
            resultado = buscar_en_indice_invertido(palabra)
    else:
        form = BusquedaForm()

    return render(request, 'Mi_buscador/buscar.html', {'form': form, 'resultado': resultado})

def buscar_en_indice_invertido(palabra):
    resultados = []

    # Ruta al archivo ind_inv_raiz.txt en el directorio static
    archivo_path = os.path.join(os.path.dirname(__file__), 'static/Mi_buscador/ind_inv_raiz.txt')

    try:
        with open(archivo_path, 'r', encoding='utf-8') as file:
            for line in file:
                palabra_archivo, data_str = line.split(" : ", 1)
                try:
                    data = ast.literal_eval(data_str.strip())
                    for url, metrica in data:
                        if palabra.lower() == palabra_archivo.lower():
                            resultados.append({'palabra': palabra_archivo, 'url': url, 'metrica': metrica})
                except (SyntaxError, ValueError):
                    # Ignorar líneas mal formateadas o que no se puedan evaluar
                    continue

        # Ordenar los resultados por la métrica de mayor a menor
        resultados = sorted(resultados, key=lambda x: x['metrica'], reverse=True)

    except FileNotFoundError:
        print(f"El archivo {archivo_path} no fue encontrado.")
        resultados = []

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        resultados = []

    return resultados
