Streetwear E-Commerce ETL Pipeline (PySpark & Docker)

Un pipeline ETL desacoplado y reproducible construido con PySpark bajo una arquitectura Medallion (Bronze / Silver / Gold). Procesa datos de catálogo e-commerce simulando un Data Lakehouse, extrayendo datos crudos desde una API REST, aplicando limpieza y tipado estricto, y generando métricas analíticas listas para consumo.

El entorno de ejecución está totalmente contenedorizado mediante Docker, eliminando dependencias locales de Python, Java OpenJDK o configuración de variables de entorno.

Arquitectura del Pipeline (Medallion Pattern)

[ API REST Escuelajs ]
         │
         ▼  (01_streetwear_extract.py)
   ┌───────────┐
   │  BRONZE   │  data/raw/streetwear_products_raw.json (Raw Ingestion)
   └─────┬─────┘
         │
         ▼  (02_streetwear_transform.py)
   ┌───────────┐
   │  SILVER   │  data/output/silver/ (Parquet limpio particionado por category_id)
   └─────┬─────┘
         │
         ▼  (03_streetwear_analytics.py)
   ┌───────────┐
   │   GOLD    │  data/output/gold/ (Métricas agregadas y rankings con Window Functions)
   └───────────┘


Capas de Datos

Bronze (Raw Ingestion): Ingesta asíncrona de datos desde la API REST en formato JSON sin alterar la estructura original.

Silver (Clean & Conformed): Validación de esquema, tipado numérico, aplanado de estructuras anidadas y particionado columnar en formato Apache Parquet.

Gold (Analytics & Aggregations): Cálculo de métricas de negocio con PySpark SQL (Window Functions dense_rank, agregaciones por categoría y clasificación por rangos de precio).

Estructura del Repositorio

.
├── 01_streetwear_extract.py     # Script capa Bronze (Extracción API REST)
├── 02_streetwear_transform.py   # Script capa Silver (Limpieza y Parquet en PySpark)
├── 03_streetwear_analytics.py   # Script capa Gold (Window functions y agregaciones)
├── 04_main_streetwear.py        # Orquestador del pipeline completo
├── Dockerfile                   # Imagen con Python 3.11 y Java JRE (PySpark ready)
├── requirements.txt             # Dependencias mínimas fijadas
├── .gitignore                   # Exclusión estricta de datasets y cachés
└── data/                        # Estructura del Data Lakehouse (rastreada con .gitkeep)
    ├── raw/
    └── output/
        ├── silver/
        └── gold/


Ejecución Rápida con Docker (Recomendado)

No requiere instalar Java, Spark ni configurar entornos virtuales locales. Únicamente necesitas tener instalado y activo Docker Desktop.

1. Clonar el repositorio

git clone <URL_DE_TU_REPOSITORIO>
cd streetwear_etl


2. Construir la imagen Docker

docker build -t streetwear-etl .


3. Ejecutar el pipeline

Para que los archivos generados en las capas Bronze, Silver y Gold persistan en tu máquina local, ejecuta el contenedor montando el volumen de datos:

docker run --rm -v "$(pwd)/data:/app/data" streetwear-etl


El pipeline ejecutará automáticamente el orquestador (04_main_streetwear.py), mostrando en consola el progreso de cada etapa y volcando los datasets finales en la carpeta local data/.

Ejecución en Entorno Local (Alternativa)

Si prefieres ejecutar el pipeline directamente en tu entorno local sin Docker:

Requisitos previos

Python 3.10+

Java OpenJDK 17 o superior (requerido para ejecutar PySpark localmente)

Pasos

# 1. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Lanzar orquestador
python 04_main_streetwear.py


Métricas Producidas (Capa Gold)

El pipeline genera tres datasets analíticos en data/output/gold/:

category_metrics/: Resumen analítico por categoría (precio promedio, precio mínimo, precio máximo y volumen de catálogo).

tier_metrics/: Segmentación de productos en rangos comerciales (Budget, Mid, Premium).

ranked_products/: Ranking ordenado de productos más caros dentro de cada categoría calculados mediante funciones de ventana (Window.partitionBy().orderBy())