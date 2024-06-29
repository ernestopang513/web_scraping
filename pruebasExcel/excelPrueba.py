import pandas as pd
from datetime import datetime

# Crear un DataFrame con la fecha guardada
fecha_guardada = "10/06/2024 18:36"
df = pd.DataFrame({'Fecha': [fecha_guardada]})

# Guardar el DataFrame en un archivo Excel
df.to_excel("fechas_pandas.xlsx", index=False)

# Pedir al usuario que ingrese otra fecha
fecha_usuario = input("Ingrese una fecha (día/mes/año hora:minutos): ")
fecha_usuario_dt = datetime.strptime(fecha_usuario, "%d/%m/%Y %H:%M")
fecha_guardada_dt = datetime.strptime(fecha_guardada, "%d/%m/%Y %H:%M")

# Comparar las fechas
if fecha_usuario_dt > fecha_guardada_dt:
    print(f"La fecha ingresada ({fecha_usuario}) es posterior a la fecha guardada ({fecha_guardada}).")
elif fecha_usuario_dt < fecha_guardada_dt:
    print(f"La fecha ingresada ({fecha_usuario}) es anterior a la fecha guardada ({fecha_guardada}).")
else:
    print(f"La fecha ingresada ({fecha_usuario}) es igual a la fecha guardada ({fecha_guardada}).")
