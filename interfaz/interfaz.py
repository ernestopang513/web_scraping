import customtkinter as ctk
from utilidades.utilidades  import buscarActualizaciones,fecha_inicial

from interfaz.pages.encino_page import encino_page

def crear_interfaz():
    # Configuración de la apariencia global
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")  # Temas: "blue", "green", "dark-blue"

    # Crear la ventana principal
    root = ctk.CTk()
    root.title("Obtención de datos El Encino")
    root.geometry("800x300")

    # Paleta de colores CFE
    global negro_cfe 
    negro_cfe = "#000000"
    global verde_cfe 
    verde_cfe = "#008A57"
    blanco_cfe = "#FFFFFF"
    global gris_cfe 
    gris_cfe = "#A5A5A5"
    global gris_claro 
    gris_claro = "#F0F0F0"


    opciones_frame = ctk.CTkFrame(root, fg_color=gris_cfe, width= 100)

    #Situa el frame a la izquieta
    opciones_frame.pack(side = ctk.LEFT, fill = "y")
    
    # Lo siguiente manda todito a la derecha
    #opciones_frame.pack(anchor= "w")
    principal_frame = ctk.CTkFrame(root, fg_color= blanco_cfe )
    
    principal_frame.pack(side = ctk.LEFT, expand = True, fill = ctk.BOTH)
    # principal_frame.pack( anchor = ctk.W, fill = "y")
    inicio_page(principal_frame)

    def menu_click(funcion, principal_frame ,btn, *args ):
        for item in args:
            item.configure(fg_color = 'green', state= ctk.NORMAL)
        # print (f"{principal_frame.winfo_children()}")
        for frame in principal_frame.winfo_children():
            frame.destroy()

        btn.configure(fg_color = 'red',state = ctk.DISABLED)
        funcion(principal_frame)
        


    inicio_btn = ctk.CTkButton(opciones_frame, text= 'Inicio', command=lambda : menu_click(inicio_page, principal_frame, inicio_btn, encino_btn))
    inicio_btn.pack(side = ctk.TOP, expand = True)
    
    encino_btn = ctk.CTkButton(opciones_frame, text= 'Encino 1',command=lambda : menu_click(encino_page, principal_frame, encino_btn, inicio_btn ))
    encino_btn.pack(side = ctk.TOP, expand = True)




    # Ejecutar el bucle principal de la ventana
    root.mainloop()


def inicio_page(principal_frame):

    inicio_frame = ctk.CTkFrame(principal_frame) 

    label = ctk.CTkLabel(inicio_frame, text='Inicio', font=("Arial", 16), text_color=verde_cfe)
    label.pack(padx =20, pady=10, anchor = ctk.N, side = ctk.LEFT)

    inicio_frame.pack(side = ctk.LEFT, expand = True, fill = ctk.BOTH)