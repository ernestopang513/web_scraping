import customtkinter as ctk
from utilidades.utilidades  import buscarActualizaciones

def crear_interfaz():
    # Configuración de la apariencia global
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")  # Temas: "blue", "green", "dark-blue"

    # Crear la ventana principal
    root = ctk.CTk()
    root.title("Obtención de datos El Encino")
    root.geometry("400x300")

    # Paleta de colores CFE
    negro_cfe = "#000000"
    verde_cfe = "#006341"
    blanco_cfe = "#FFFFFF"
    gris_cfe = "#A5A5A5"

    # Crear una etiqueta
    label = ctk.CTkLabel(root, text="Última fecha de evento guardada", font=("Arial", 16), text_color=verde_cfe)
    label.pack(pady=10, anchor="w")

    # Crear una etiqueta para la última fecha
    ultimaFecha_label = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=gris_cfe)
    ultimaFecha_label.pack(anchor="w")

    # Crear un botón para buscar actualizaciones
    # buttonBuscaActualizaciones = ctk.CTkButton(root, text="Buscar Actualizaciones El Encino", command= lambda : buscarActualizaciones(etiqueta_resultado,buttonBuscaActualizaciones))
    buttonBuscaActualizaciones = ctk.CTkButton(root, text="Buscar Actualizaciones El Encino", command= lambda : buscarActualizaciones(etiqueta_resultado,buttonBuscaActualizaciones,etiqueta_aviso))
    buttonBuscaActualizaciones.pack(pady=10, anchor="w")

    # Crear una etiqueta para el resultado
    #global etiqueta_resultado
    etiqueta_resultado = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=negro_cfe)
    etiqueta_resultado.pack(pady=10, anchor="w")
    
    etiqueta_aviso = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=gris_cfe)
    etiqueta_aviso.pack(pady=10, anchor="w")

    # Ejecutar el bucle principal de la ventana
    root.mainloop()
