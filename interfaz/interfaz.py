import customtkinter as ctk
from utilidades.utilidades  import buscarActualizaciones,fecha_inicial

def crear_interfaz():
    # Configuración de la apariencia global
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")  # Temas: "blue", "green", "dark-blue"

    # Crear la ventana principal
    root = ctk.CTk()
    root.title("Obtención de datos El Encino")
    root.geometry("800x300")

    # Paleta de colores CFE
    negro_cfe = "#000000"
    verde_cfe = "#008A57"
    blanco_cfe = "#FFFFFF"
    gris_cfe = "#A5A5A5"

    # Crear una etiqueta de titulo
    label = ctk.CTkLabel(root, text="Última fecha de evento guardada", font=("Arial", 16), text_color=verde_cfe)
    label.pack(padx =20, pady=10, anchor="w")

    # Crear una etiqueta para la última fecha
    ultimaFecha_label = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=negro_cfe)
    ultimaFecha_label.pack(anchor="w", padx =20)
    fecha_inicial(ultimaFecha_label)

    # Crear un botón para buscar actualizaciones
    
    buttonBuscaActualizaciones = ctk.CTkButton(
        root, 
        height= 20,
        width= 200,
        #hover_color= "white", 
        text="Buscar Actualizaciones El Encino", 
        command= lambda : buscarActualizaciones(etiqueta_resultado,buttonBuscaActualizaciones,etiqueta_aviso, ultimaFecha_label),
        fg_color=verde_cfe,
        #corner_radius= 100
        )
  
    buttonBuscaActualizaciones.pack(padx = 20 , anchor= "w")
    

    # Crear una etiqueta para el resultado
    etiqueta_resultado = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=negro_cfe)
    etiqueta_resultado.pack(pady=10, anchor="w", padx = 20)
    
    #El texto de la 'etiqueta aviso' se genera en la funcion abrir_y_procesar_excel pero es insertado en la funcion buscarActualizaciones 

    etiqueta_aviso = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color=gris_cfe, justify = ctk.LEFT)
    etiqueta_aviso.pack(pady=10, anchor="w", padx = 20)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()
