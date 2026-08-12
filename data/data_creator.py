import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generar_dataset_streetwear(num_filas=5000, output_path="data/sales_raw.csv"):
    print(f"[GENERADOR] Creando dataset de streetwear con {num_filas} registros...")

    # Catálogo de prendas/sneakers con precios base promedio (€)
    catalogo = {
        'Heavyweight Oversize Tee 300 GSM': 45.0,
        'Boxy Fit Hoodie 500 GSM': 90.0,
        'Cargo Pants Baggy Fit': 85.0,
        'ASICS GEL-NYC Tech Runner': 150.0,
        'New Balance 990v3 Made in USA': 220.0,
        'Puffer Jacket Limited Release': 180.0,
        'Graphic Zip-Up Hoodie': 95.0,
        'Denim Shorts Wide Leg': 65.0
    }
    
    prendas = list(catalogo.keys())
    canales_tiendas = ['Drop Online Global', 'Pop-Up Store Madrid', 'Retail Partner', 'Flagship Store']
    
    # Fechas a lo largo de los meses de 2026
    fecha_inicio = datetime(2026, 1, 1)

    datos = []

    for _ in range(num_filas):
         prenda = random.choice(prendas)
         precio_base = catalogo[prenda]
         
         # Cliente/Canal con espacios extra para probar str.strip()
         canal = f"  {random.choice(canales_tiendas)}  "
         
         # Fechas aleatorias
         dias_random = random.randint(0, 220)
         fecha = (fecha_inicio + timedelta(days=dias_random)).strftime('%Y-%m-%d')

         # Cantidad con nulos (-1 o NaN) para probar el filtro de calidad
         cantidad = random.choice([1, 1, 1, 2, 3, 5, np.nan, -1])
         
         # Coste de producción aproximado (35%-50% del precio de venta)
         coste_unitario = round(precio_base * random.uniform(0.35, 0.50), 2)

         # Inyección de símbolos $, € y algunos errores de precio negativo
         prob = random.random()
         if prob < 0.35:
             precio_unitario = f"${precio_base}"
         elif prob < 0.70:
             precio_unitario = f"{precio_base} €"
         elif prob < 0.96:
             precio_unitario = precio_base
         else:
             precio_unitario = -45.0  # Registro corrupto

         datos.append({
             'Fecha Venta': fecha,
             'Cliente': canal,
             'Producto': prenda,
             'Cantidad': cantidad,
             'Precio Unitario': precio_unitario,
             'Coste Unitario': coste_unitario
         })

    # Crear el DataFrame y exportarlo a CSV
    df_raw = pd.DataFrame(datos)
    df_raw.to_csv(output_path, index=False)
    print(f"[GENERADOR] ¡Dataset de streetwear creado con éxito en: {output_path}!")

if __name__ == "__main__":
    generar_dataset_streetwear(num_filas=5000)