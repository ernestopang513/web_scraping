import customtkinter as ctk

def crear_interfaz():
    # Configuración de la apariencia global
    ctk.set_appearance_mode("dark")  # Modos: "light", "dark", "system"
    ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

    # Crear la ventana principal
    root = ctk.CTk()
    root.title("Todos los Labels a la Izquierda")
    root.geometry("500x400")

    # Crear un Frame como contenedor para todos los labels
    frame_izquierda = ctk.CTkFrame(root, corner_radius=15)
    frame_izquierda.pack(side=ctk.LEFT, fill=ctk.Y, padx=20, pady=20, expand=True)

    # Crear y agregar los Labels al frame_izquierda
    label1 = ctk.CTkLabel(frame_izquierda, text="Label 1", font=("Arial", 16))
    label1.pack(anchor="w", pady=5)

    label2 = ctk.CTkLabel(frame_izquierda, text="Label 2", font=("Arial", 16))
    label2.pack(anchor="w", pady=5)

    label3 = ctk.CTkLabel(frame_izquierda, text="Label 3", font=("Arial", 16))
    label3.pack(anchor="w", pady=5)

    label4 = ctk.CTkLabel(frame_izquierda, text="Label 4", font=("Arial", 16))
    label4.pack(anchor="w", pady=5)

    # Añadir un título decorativo
    titulo = ctk.CTkLabel(root, text="Interfaz de Usuario Mejorada", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # Añadir un botón decorativo
    boton = ctk.CTkButton(root, text="Click Me", font=("Arial", 16))
    boton.pack(pady=20)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

crear_interfaz()
