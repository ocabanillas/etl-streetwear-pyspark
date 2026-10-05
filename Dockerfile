FROM python:3.11-slim

# Instalar Java JRE headless y procps necesarios para PySpark
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre-headless \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Configurar JAVA_HOME dinámicamente apuntando a default-java
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

WORKDIR /app

# Copiar dependencias e instalarlas en capa cacheable
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Comando por defecto: orquestador del pipeline
CMD ["python", "04_main_streetwear.py"]