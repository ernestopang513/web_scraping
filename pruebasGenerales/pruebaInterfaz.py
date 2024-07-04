import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Función que se llama cuando se hace clic en el botón
def comparar_y_mostrar():
    fecha_usuario = entrada_fecha.get()
    try:
        fecha_usuario_dt = datetime.strptime(fecha_usuario, "%d/%m/%Y %H:%M")
        etiqueta_resultado.config(text=f"Has ingresado: {fecha_usuario_dt}")
    except ValueError:
        messagebox.showerror("Formato de Fecha Incorrecto", "Por favor, ingrese la fecha en el formato 'día/mes/año hora/minutos'.")

# Crear la ventana principal
root = tk.Tk()
root.title("Obtencion de datos El Encino")
root.geometry("300x400")

# Crear una etiqueta
label = tk.Label(root, text="Ingrese una fecha (día/mes/año hora/minutos):")
label.pack(pady=10)

# Crear una entrada de texto
entrada_fecha = tk.Entry(root)
entrada_fecha.pack(pady=10)

# Crear un botón y asociarlo con la función comparar_y_mostrar
button = tk.Button(root, text="Comparar y Mostrar", command=comparar_y_mostrar)
button.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
root.mainloop()
