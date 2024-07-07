import pandas as pd
from datetime import datetime
import os
from tkinter import messagebox
from datetime import datetime
import threading
from extraccionDatos.extractionWeb import verifica_actualizaciones


def verifica_existencia_excel(ruta_relativa):
    # ruta_relativa = 
    ruta_absoluta = os.path.join(os.path.dirname(__file__), "..", ruta_relativa)
    return os.path.exists(ruta_absoluta)


def abrir_y_procesar_excel(ruta_relativa, fecha_usuario):
    
    if verifica_existencia_excel(ruta_relativa):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), "..", ruta_relativa)
        df = pd.read_excel(ruta_absoluta)
        print("Contenido del archivo Excel:")
        print(df)

        # Leer la fecha guardada en el DataFrame
        fecha_guardada = df.loc[0, 'Fecha']

        # Convertir la fecha guardada a un objeto datetime
        fecha_guardada_dt = datetime.strptime(fecha_guardada, "%d/%m/%Y %H:%M")

        # Convertir la fecha ingresada por el usuario a un objeto datetime
        fecha_usuario_dt = datetime.strptime(fecha_usuario, "%d/%m/%Y %H:%M")

        # Comparar las fechas
        if fecha_usuario_dt > fecha_guardada_dt:
            # Reemplazar la fecha en el DataFrame
            os.chdir("../data")
            df.loc[0, 'Fecha'] = fecha_usuario_dt.strftime("%d/%m/%Y %H:%M")
            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel("fechas_pandas.xlsx", index=False)
            return f"La fecha obteida de la web ({fecha_usuario}) es posterior a la fecha guardada ({fecha_guardada}). La fecha guardada ha sido actualizada."
        elif fecha_usuario_dt < fecha_guardada_dt:
            return f"La fecha obteida de la web ({fecha_usuario}) es anterior a la fecha guardada ({fecha_guardada})."
        else:
            return f"La fecha obteida de la web ({fecha_usuario}) es igual a la fecha guardada ({fecha_guardada})."
        
        
    else:
        print(f"El archivo {ruta_relativa} no existe se creó uno.")

        os.chdir(os.path.join(os.path.dirname(__file__), "..", 'data'))

        df = pd.DataFrame({'Fecha': [fecha_usuario]})

        df.to_excel("fechas_pandas.xlsx", index =False)

        os.chdir('..')

      

        return fecha_usuario
    


def buscarActualizaciones(etiqueta_resultado, buttonBuscaActualizaciones, etiqueta_aviso):
    etiqueta_resultado.configure(text="Buscando actualizaciones...")
    
    def tarea():
        buttonBuscaActualizaciones.configure(state="disabled")
        try:
            fecha = verifica_actualizaciones('http://www.tcmas.mx/')
            ruta_relativa = os.path.join("data", "fechas_pandas.xlsx")
            mensaje = abrir_y_procesar_excel(ruta_relativa, fecha)
            
            etiqueta_resultado.configure(text=f"Fecha guardada: {fecha}")
            etiqueta_aviso.configure(text=mensaje)

        except Exception as e:
            messagebox.showerror(message=f"Algo salió mal {e}", title="Error")
        finally:
            buttonBuscaActualizaciones.configure(state="normal")
    hilo = threading.Thread(target=tarea)
    hilo.start()

        