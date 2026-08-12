import pandas as pd 
from config import get_engine
#importamos la funcion get engine que creamos en la config
#este fichero carga los datos limpios en nuestra bd

def load_to_postgres(df: pd.DataFrame, table_name: str = 'fact_sales'):
    engine = get_engine()
    print(f"[LOAD] Inserting {len(df)} records into the table '{table_name}'...")
    #creamos la funcion donde le indicamos que los datos vienen de un DF
    #estos se volcaran en la tabla fact, engine es el motor de busqueda hacia la DB
    #con el print vemos la cantidad de datos que va a insertar en la tabla el len
    #es lo que que nos permite ver la cartidas

    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False,
            chunksize=1000
        )
        print(f"[LOAD] Successfully inserted {len(df)} records into '{table_name}'.")

        #Convertimos el DF en una tabla en nuestra BD, la tabla de destino es fact_sales
        # le indicamos la conexion, si existe que la remplace y que inserte de 1000 en 1000 filas
    except Exception as e:
        print(f'[LOAD ERROR] Fail on the load process')
        raise
        #muestra error si algo falla y con raise detenemos el proceso
