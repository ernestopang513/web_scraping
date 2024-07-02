import os
from utilidades import *
from extractionWeb import verifica_actualizaciones



def comparar_y_reemplazar_fecha():
    
    ruta_relativa = os.path.join("data", "fechas_pandas.xlsx")

    url = 'http://www.tcmas.mx/'

    fecha_usuario = verifica_actualizaciones(url)

    return abrir_y_procesar_excel(ruta_relativa,fecha_usuario)
    

    

#fecha_usuario='30/06/2024 1:45'

resultado = comparar_y_reemplazar_fecha()

print(resultado)

#Path de trabajo
#print(os.getcwd())

