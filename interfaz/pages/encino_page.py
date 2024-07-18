import customtkinter as ctk

global negro_cfe 
negro_cfe = "#000000"
global verde_cfe 
verde_cfe = "#008A57"
blanco_cfe = "#FFFFFF"
global gris_cfe 
gris_cfe = "#A5A5A5"
global gris_claro 
gris_claro = "#F0F0F0"

def encino_page(principal_frame):

    encino_frame = ctk.CTkFrame(principal_frame)
    


    # Crear una etiqueta
    label = ctk.CTkLabel(encino_frame, text="Última fecha de evento guardada", font=("Arial", 16), text_color=verde_cfe)
    label.pack(padx =20, pady=10, anchor="w")

    
    ultimaFecha_label = ctk.CTkLabel(encino_frame, text="", font=("Arial", 14), text_color=negro_cfe)
    ultimaFecha_label.pack(anchor="w", padx =20)

    buttonBuscaActualizaciones = ctk.CTkButton(
        encino_frame, 
        height= 20,
        width= 200,
        text="Buscar Actualizaciones El Encino", 
        #command= lambda : buscarActualizaciones(etiqueta_resultado,buttonBuscaActualizaciones,etiqueta_aviso),
        command= lambda : print("Click en buscar actualizaciones"),
        fg_color=verde_cfe,
    
        )

    buttonBuscaActualizaciones.pack(padx = 20 , anchor= "w")
    

    
    etiqueta_resultado = ctk.CTkLabel(encino_frame, text="", font=("Arial", 14), text_color=negro_cfe)
    etiqueta_resultado.pack(pady=10, anchor="w", padx = 20)
    
    etiqueta_aviso = ctk.CTkLabel(encino_frame, text="", font=("Arial", 14), text_color=gris_cfe)
    etiqueta_aviso.pack(pady=10, anchor="w", padx = 20)
    encino_frame.pack(side = ctk.LEFT , expand = True, fill = 'both')