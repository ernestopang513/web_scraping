import os
from utilidades import *




def comparar_y_reemplazar_fecha(fecha_usuario):
    
    ruta_relativa = os.path.join("data", "fechas_pandas.xlsx")

    return abrir_y_procesar_excel(ruta_relativa,fecha_usuario)
    

    

fecha_usuario='30/06/2024 1:45'

resultado = comparar_y_reemplazar_fecha(fecha_usuario)

print(resultado)

print(os.getcwd())

