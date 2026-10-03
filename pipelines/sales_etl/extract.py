import pandas as pd
#este script se encarga de la extracción de datos

def extract_raw_sales(file_path: str) -> pd.DataFrame:
    """Define la función extract_raw_sales que recibe una ruta de archivo 
    (file_path) y devuelve un DataFrame de Pandas."""
    try:

        print(f"[EXTRACT] reading data from: {file_path}")
        df = pd.read_csv(file_path)
        print(f"[EXTRACT] extracted rows: {len(df)}")
        return df
        #Nos muestra el fichero que está leyendo, lo guardamos en DF, cuenta el numero de filas
        #y nos devuelve el DF
    
    except FileNotFoundError:
        print(f"[EXTRACT ERROR] The file {file_path} does not exist.")
        raise
        #raise detiene el script de forma controlada
