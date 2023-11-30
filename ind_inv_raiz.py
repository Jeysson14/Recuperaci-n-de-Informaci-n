import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

archivo = "urls.txt"
salida_txt = "ind_inv_ind.txt"

resultados = {}

def obtener_palabras(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    except Exception as e:
        return []

with open(archivo, 'r') as file:
    urls = file.read().splitlines()

for url in urls:
    words = obtener_palabras(url)

    for word in words:
        if word not in resultados:
            resultados[word] = []

        resultados[word].append((url, words.count(word)))

with open(salida_txt, 'w') as file:
    for word, data in resultados.items():
        file.write(f"{word} : {data}\n")

print(f"Archivo guardado")