Este proyecto esta hecho en Django, primero se creo el proyecto llamado Buscador y despues una app llamada Mi_buscador.

Se Modificaron los archivos 
*views.py
*settings.py
*urls.py

Ademas de que se crearon los archivos
*forms.py
*buscar.html
*base_generic.html

El archivo llamado ind_inv_raiz.txt se añadio a la carpeta de static para poder acceder a el desde el archivo views.txt que 
contiene toda la logica de busqueda del programa, en el archivo de settings.py se agrego la app y en los archivos de urls.py 
se agregaron las direcciones para poder acceder a todos los archivos y el archivo de buscar.html muestra la salida de la busqueda 
de las palabras de la siguiente forma

[
    {'palabra': 'python', 'url': 'http://www.ejemplo1.com', 'metrica': 10},
    {'palabra': 'python', 'url': 'http://www.ejemplo2.com', 'metrica': 5},
    {'palabra': 'python', 'url': 'http://www.ejemplo3.com', 'metrica': 3},
]
