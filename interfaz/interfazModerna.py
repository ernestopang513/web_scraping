import customtkinter as ctk

def crear_interfaz():
    # Crear la ventana principal
    root = ctk.CTk()
    root.title("Todos los Labels a la Izquierda")
    root.geometry("400x300")

    # Crear un Frame como contenedor para todos los labels
    frame_izquierda = ctk.CTkFrame(root)
    frame_izquierda.pack(side=ctk.LEFT, fill=ctk.Y, padx=20, pady=20)

    # Crear y agregar los Labels al frame_izquierda
    label1 = ctk.CTkLabel(frame_izquierda, text="Label 1")
    label1.pack(anchor="w")

    label2 = ctk.CTkLabel(frame_izquierda, text="Label 2")
    label2.pack(anchor="w")

    label3 = ctk.CTkLabel(frame_izquierda, text="Label 3")
    label3.pack(anchor="w")

    label4 = ctk.CTkLabel(frame_izquierda, text="Label 4")
    label4.pack(anchor="w")

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

crear_interfaz()
