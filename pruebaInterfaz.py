import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from extraccionDatos.extractionWeb import verifica_actualizaciones


def buscarActualizaciones():
    etiqueta_resultado.config(text=f"Buscarndo actualizaciones...")
    fecha = verifica_actualizaciones('http://www.tcmas.mx/')
    try:
        etiqueta_resultado.config(text=f"fecha guadada: {fecha}")
    except:
        messagebox.showerror(message="Algo salio mal", title="Error")


# Crear la ventana principal
root = tk.Tk()
root.title("Obtencion de datos El Encino")
root.geometry("300x400")



label = tk.Label(root, text="Ultima fecha de evento guardada")
label.pack(pady=10, anchor="w")


ultimaFecha_label = tk.Label(root, text = "")
ultimaFecha_label.pack(anchor="w")

buttonBuscaActualizaciones = tk.Button(root, text="Buscar Actualizaciones El Encino", command=buscarActualizaciones)
buttonBuscaActualizaciones.pack(pady=10, anchor="w")


etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack( ipady=0,pady=0, anchor="w")

# Ejecutar el bucle principal de la ventana
root.mainloop()
