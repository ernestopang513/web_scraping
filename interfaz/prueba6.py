import tkinter as tk

def crear_interfaz():
    root = tk.Tk()
    root.title("Todos los Labels a la Izquierda")
    root.geometry("400x300")

    # Crear un Frame como contenedor para todos los labels
    frame_izquierda = tk.Frame(root)
    frame_izquierda.pack(side="left", fill=tk.Y, padx=20, pady=20)

    # Crear y agregar los Labels al frame_izquierda
    label1 = tk.Label(frame_izquierda, text="Label 1",bg="lightgrey")
    label1.pack(anchor="se")

    label2 = tk.Label(frame_izquierda, text="Label 2")
    label2.pack(anchor="w")

    label3 = tk.Label(frame_izquierda, text="Label 3")
    label3.pack(anchor="w")

    label4 = tk.Label(frame_izquierda, text="Label 4")
    label4.pack(anchor="e")

    root.mainloop()

crear_interfaz()
