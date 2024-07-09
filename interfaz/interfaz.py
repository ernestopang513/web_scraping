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
    gris_claro = "#F0F0F0"


    opciones_frame = ctk.CTkFrame(root, fg_color=gris_cfe, width= 100)

    #Situa el frame a la izquieta
    opciones_frame.pack(side = ctk.LEFT, fill = "y")
    
    # Lo siguiente manda todito a la derecha
    #opciones_frame.pack(anchor= "w")
    principal_frame = ctk.CTkFrame(root, fg_color=blanco_cfe )
    principal_frame.pack(side = ctk.LEFT, expand = True, fill = ctk.BOTH)
    # principal_frame.pack( anchor = ctk.W, fill = "y")

    # Crear una etiqueta
    label = ctk.CTkLabel(principal_frame, text="Última fecha de evento guardada", font=("Arial", 16), text_color=verde_cfe)
    label.pack(padx =20, pady=10, anchor="w")

    
    ultimaFecha_label = ctk.CTkLabel(principal_frame, text="", font=("Arial", 14), text_color=negro_cfe)
    ultimaFecha_label.pack(anchor="w", padx =20)

    buttonBuscaActualizaciones = ctk.CTkButton(
        principal_frame, 
        height= 20,
        width= 200,
        
        text="Buscar Actualizaciones El Encino", 
        #command= lambda : buscarActualizaciones(etiqueta_resultado,buttonBuscaActualizaciones,etiqueta_aviso),
        command= lambda : print("Click en buscar actualizaciones"),
        fg_color=verde_cfe,
      
        )
  
    buttonBuscaActualizaciones.pack(padx = 20 , anchor= "w")
    

    
    etiqueta_resultado = ctk.CTkLabel(principal_frame, text="", font=("Arial", 14), text_color=negro_cfe)
    etiqueta_resultado.pack(pady=10, anchor="w", padx = 20)
    
    etiqueta_aviso = ctk.CTkLabel(principal_frame, text="", font=("Arial", 14), text_color=gris_cfe)
    etiqueta_aviso.pack(pady=10, anchor="w", padx = 20)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()
