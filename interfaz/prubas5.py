import tkinter as tk

def crear_interfaz():
    root = tk.Tk()
    root.title("Contenedor para Label Izquierda")
    root.geometry("400x300")

    # Crear un Frame como contenedor para el label_izquierda
    frame_izquierda = tk.Frame(root, bg="lightgrey", padx=10, pady=10)
    frame_izquierda.pack(side="top", padx=20, pady=20)

    # Crear el Label y agregarlo al frame_izquierda
    label_izquierda = tk.Label(frame_izquierda, text="Izquierda")
    label_izquierda.pack()

    # Crear otro Label en el root para mostrar comparación
    label_derecha = tk.Label(root, text="Derecha")
    label_derecha.pack(side=tk.RIGHT, padx=20)

    root.mainloop()

crear_interfaz()
