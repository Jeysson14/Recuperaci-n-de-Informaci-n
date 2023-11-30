import tkinter as tk
from tkinter import scrolledtext
import ast

class BuscadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Buscador de Palabras")

        self.etiqueta = tk.Label(master, text="Ingrese la palabra:")
        self.etiqueta.pack()

        self.entrada = tk.Entry(master)
        self.entrada.pack()

        self.boton = tk.Button(master, text="Buscar", command=self.buscar)
        self.boton.pack()

        self.resultados_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.resultados_text.pack()

    def buscar(self):
        palabra_buscar = self.entrada.get().lower()

        resultados = self.obtener_resultados(palabra_buscar)

        self.resultados_text.delete(1.0, tk.END)  # Limpiar el área de resultados

        for resultado in resultados:
            self.resultados_text.insert(tk.END, f"Palabra: {resultado['palabra']}\n")
            self.resultados_text.insert(tk.END, f"URL: {resultado['url']}\n")
            self.resultados_text.insert(tk.END, f"Métrica: {resultado['metrica']}\n\n")

    def obtener_resultados(self, palabra_buscar):
        resultados = []

        with open("raiz_ind_inv.txt", "r", encoding="utf-8") as file:
            for line in file:
                palabra, data_str = line.split(" : ", 1)
                try:
                    data = ast.literal_eval(data_str.strip())  # Utilizar ast.literal_eval
                    for url, metrica in data:
                        if palabra.lower() == palabra_buscar.lower():
                            resultados.append({"palabra": palabra, "url": url, "metrica": metrica})
                except (SyntaxError, ValueError):
                    # Ignorar líneas mal formateadas o que no se puedan evaluar
                    continue

        # Ordenar los resultados por la métrica de mayor a menor
        resultados = sorted(resultados, key=lambda x: x["metrica"], reverse=True)

        return resultados

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorApp(root)
    root.mainloop()
