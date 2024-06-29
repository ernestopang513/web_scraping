import pandas as pd
from datetime import datetime
import os


#fecha_usuario = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
def verifica_existencia_excel(ruta_relativa):
    ruta_absoluta = os.path.join(os.path.dirname(__file__), ruta_relativa)
    return os.path.exists(ruta_absoluta)

def abrir_y_procesar_excel(ruta_relativa, fecha_usuario):
    
    if verifica_existencia_excel(ruta_relativa):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), ruta_relativa)
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
            df.loc[0, 'Fecha'] = fecha_usuario_dt.strftime("%d/%m/%Y %H:%M")
            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel("fechas_pandas.xlsx", index=False)
            return f"La fecha ingresada ({fecha_usuario}) es posterior a la fecha guardada ({fecha_guardada}). La fecha guardada ha sido actualizada."
        elif fecha_usuario_dt < fecha_guardada_dt:
            return f"La fecha ingresada ({fecha_usuario}) es anterior a la fecha guardada ({fecha_guardada})."
        else:
            return f"La fecha ingresada ({fecha_usuario}) es igual a la fecha guardada ({fecha_guardada})."
        
        # Aquí puedes agregar el código adicional para procesar el DataFrame
    else:
        print(f"El archivo {ruta_relativa} no existe.")


def comparar_y_reemplazar_fecha(fecha_usuario):
    
    ruta_relativa = os.path.join("data", "fechas_pandas.xlsx")

    return abrir_y_procesar_excel(ruta_relativa,fecha_usuario)
    

    
# Ejemplo de uso
#fecha_usuario = input("Ingrese una fecha (día/mes/año hora:minutos): ")
fecha_usuario='30/06/2024 1:45'

resultado = comparar_y_reemplazar_fecha(fecha_usuario)

print(resultado)