import pandas as pd
from datetime import datetime

fecha_usuario='30/06/2024 1:45'
#fecha_usuario = datetime.strptime(fecha, "%d/%m/%Y %H:%M")

def comparar_y_reemplazar_fecha(fecha_usuario):
    """
    Compara una fecha ingresada por el usuario con una fecha guardada en un archivo Excel.
    Si la fecha ingresada es posterior a la fecha guardada, la reemplaza en el archivo Excel.

    Args:
    fecha_usuario (str): Fecha ingresada por el usuario en el formato "día/mes/año hora:minutos".

    Returns:
    str: Un mensaje indicando si la fecha ingresada es anterior, posterior o igual a la fecha guardada.
    """
    # Abrir el archivo Excel existente y leer la fecha
    df = pd.read_excel("fechas_pandas.xlsx")

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

# Ejemplo de uso
#fecha_usuario = input("Ingrese una fecha (día/mes/año hora:minutos): ")
resultado = comparar_y_reemplazar_fecha(fecha_usuario)
print(resultado)
