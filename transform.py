import pandas as pd
import numpy as np
#este script se encarga de la limpieza de datos

def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    print('[transform] startting transformation pipeline')
    df = df.copy()
# Creamos una funcion donde le indicamos que el origen es un DF de pandas
# y la salida tendra el mismo formato, 
# creamos una copia para no modificar los datos originales

    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
# en la cabecera de las oolumnas eliminamos espacios en blanco, 
# letras a miniscula y cambiamos espacios por _

    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], errors='coerce')
    # convierte el texto de ese campo a formato YYYY-MM-DD si la fecha está en mal formato
    # error coerce la da como nula

    if df['precio_unitario'].dtype == 'object':
       df['precio_unitario'] = df['precio_unitario'].astype(str).str.replace(r'[\$,€]', '', regex=True)

    df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')
    """comprobamos si la columna viene en formato texto, buscamos los signos de $ y euro
    y los eliminamos, el regex le indica que $ es el formarto y no string
    despues convertimos ya el texto limpio a formato decimal"""

    df['cantidad'] = df['cantidad'].fillna(1).astype(int)
    df = df[(df['precio_unitario'] > 0) & (df['cantidad'] > 0)].copy()
    #si la cantidad es nula o vacia asume el valor de 1, 
    # indicando que los numeros deben ser enteros sin decimales
    # y le indicamos que el precio y cantidad debe ser mayor que 0

    df['ingreso_total'] = np.round(df['precio_unitario'] * df['cantidad'], 2)
    df['coste_total'] = np.round(df['cantidad'] * df['coste_unitario'], 2)
    df['beneficio_neto'] = np.round(df['ingreso_total'] - df['coste_total'], 2)
    df['margen_porcentaje'] = np.round((df['beneficio_neto'] / df['ingreso_total']) * 100, 2)
    # calculamos y por ultimo redondeamos el porcentaje del margen a 2 decimales

    df['categoria_tickets'] = 'Valor bajo'
    df.loc[df['ingreso_total'] >= 150, 'categoria_tickets'] = 'valor medio'
    df.loc[df['ingreso_total'] >=500, 'categoria_tickets'] = 'valor alto'
    #creamos la columna y le asignamos el valor mas bajo 
    #lo que hacemos con .loc es sobreescribirlas indicando que si es mayor
    # a 150 sea valor medio y mayor a 500 valor alto

    print(f"[TRANSFORM] Completed transformation. Processed records: {len(df)}")
    return df
    # nos indica la cantidad de datos que hemos limpiado 