# 📊 ETL E-Commerce Sales Pipeline

Pipeline de datos **ETL (Extract, Transform, Load)** automatizado en Python para procesar registros de ventas e-commerce y cargarlos en una base de datos PostgreSQL en un contenedor Docker.

## 🚀 Arquitectura del Proyecto

* **Extract (`extract.py`):** Lectura e ingesta de datos brutos desde archivos CSV.
* **Transform (`transform.py`):** Limpieza de campos, formateo de fechas, cálculo de KPIs de negocio (ingreso total, coste total, beneficio neto, margen %) y redondeo a 2 decimales con NumPy.
* **Load (`load.py`):** Conexión con SQLAlchemy/psycopg2 para la carga automatizada en PostgreSQL.
* **Config (`config.py`):** Gestión de variables de entorno con `python-dotenv`.
* **Main (`main.py`):** Orquestación con medición de tiempos de ejecución y gestión de excepciones.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías:** Pandas, NumPy, SQLAlchemy, Psycopg2, Python-Dotenv
* **Base de Datos:** PostgreSQL (en Docker)
* **Contenedorización:** Docker / Docker Desktop (WSL2)

## 🗄️ Despliegue de la Base de Datos con Docker

Para levantar el entorno de PostgreSQL en el puerto `5432`:

```bash
docker run -d \
  --name postgres-container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=ecommerce \
  -p 5432:5432 \
  postgres:15

////////////////////////////////////////

  # 📊 ETL Streetwear Analytics Pipeline

Pipeline de datos **ETL (Extract, Transform, Load)** distribuido en PySpark bajo la arquitectura Medallion (Bronze, Silver y Gold) para procesar catálogos e-commerce de streetwear y persistir analíticas avanzadas en formato Parquet.

## 🚀 Arquitectura del Proyecto

* **Extract (`01_extract.py`):** Ingesta de datos brutos en crudo (Capa Bronze) asegurando la preservación del origen en formato local sin mutaciones.
* **Transform (`02_transform.py`):** Limpieza de campos, tipado de datos, tratamiento de nulos y normalización de esquema tabular (Capa Silver).
* **Analytics & Load (`03_streetwear_analytics.py`):** Cálculo de KPIs de negocio, métricas por categoría, segmentación por rangos de precio (*Budget*, *Mid-Range*, *Premium*) y ranking de artículos mediante funciones de ventana de Spark (`Window.partitionBy().orderBy()`), persistiendo las tablas finales en formato columnar Apache Parquet (Capa Gold).
* **Main (`04_main_streetwear.py`):** Orquestación secuencial end-to-end con resolución dinámica de rutas mediante `pathlib`, ejecución controlada por `subprocess` y medición de tiempos de ejecución.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Motor Distribuido:** Apache Spark / PySpark
* **Formato de Almacenamiento:** Apache Parquet
* **Librerías / Módulos:** PySpark SQL, Pathlib, Subprocess, Time

## ⚡ Ejecución del Pipeline

Para ejecutar el pipeline completo de extremo a extremo:

```bash
python pipelines/streetwear_etl/04_main_streetwear.py


## 📁 Estructura del Repositorio

```text
etl_commerce_pro/
│
├── pipelines/
│   ├── sales_etl/                     # Pipeline 1: Ventas (Pandas & PostgreSQL)
│   │   ├── extract.py                 # Ingesta desde CSV
│   │   ├── transform.py               # KPIs de rentabilidad y normalización
│   │   ├── load.py                    # Carga automatizada a PostgreSQL
│   │   ├── config.py                  # Gestión de variables de entorno
│   │   └── main.py                    # Orquestador del flujo transaccional
│   │
│   └── streetwear_etl/                # Pipeline 2: Catálogo (PySpark & Medallion)
│       ├── 01_extract.py              # Ingesta Bronze
│       ├── 02_transform.py            # Limpieza y esquema Silver
│       ├── 03_streetwear_analytics.py # Métricas de negocio y carga Gold
│       └── 04_main_streetwear.py      # Orquestador distribuido end-to-end
│
├── data/                              # Almacén local de datos (excluido en .gitignore)
│   ├── raw/                           # Datos brutos
│   └── output/                        # Salidas procesadas (Silver / Gold)
│
├── .gitignore
└── README.md 