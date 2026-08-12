import time
from extract import extract_raw_sales
from transform import transform_sales_data
from load import load_to_postgres
#este script es el orquestador donde le indicamos el orden los scripts

def run_pipeline():
    start_time = time.time()
    print('starting sales pipeline')
    #creamos la funcion que se encarga de ejecutar todo er orden 
    # guarda la hora exacta en la que comuienza el etl en start time

    try:
        raw_df = extract_raw_sales('data/sales_raw.csv')
        clean_df = transform_sales_data(raw_df)
        load_to_postgres(clean_df, table_name="fact_sales")
        #llamamos a las funciones que hemos creado anteriormnete 
        # de extraccion, limpieza y carga

        elapsed_time = round(time.time() - start_time, 2)
        #con elapsed medimos el tiempo que tarda en ejecutarse el ETL

        print("==================================================")
        print(f"✅ PIPELINE SUCESSFULLY COMPLETED {elapsed_time} SECONDS")
        print("==================================================")

    except Exception as e:
        print("==================================================")
        print(f"❌ ERROR CREATING THE PIPELINE: {e}")
        print("==================================================")

if __name__ == "__main__":
    run_pipeline()
    """if __name__ == "__main__": es el botón de encendido del script. Le dice a Python: 
    Ejecuta el ETL de golpe solo si lanzo este archivo directamente desde la 
    terminal (python main.py), pero NO lo ejecutes si otro programa solo lo 
    está importando"""