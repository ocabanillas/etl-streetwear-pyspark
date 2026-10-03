import json
import requests

#1 Indicamos el url de la API y donde queremos que descargue el fichero
api_url = API_URL = "https://api.escuelajs.co/api/v1/products/?categoryId=1"
OUTPUT_FILE = "data/raw/streetwear_products_raw.json"

print(f"Solicitando la informacion: {API_URL}...")

#2 llamada a http
response = requests.get(api_url, timeout=10)

#3 Validación de estado
response.raise_for_status()
print(f"Conexión exitosa. Código de estado: {response.status_code}")

# 4 Parsear la respuesta
# Esta API devuelve directamente una lista de productos en formato JSON
products_list = response.json()
print(f"Datos parseados. Total de artículos obtenidos: {len(products_list)}")

# 5 Persistir en data/raw/
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(products_list, f, ensure_ascii=False, indent=2)

print(f"4. Archivo guardado con éxito en: {OUTPUT_FILE}")
