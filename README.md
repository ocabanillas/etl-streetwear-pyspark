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
