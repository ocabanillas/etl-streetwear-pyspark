import os
from sqlalchemy import create_engine

"""Este script se usa para conectarnos a nuestra BD"""


DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'caban')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ecommerce")
"""os.getenv("VARIABLE", "valor_por_defecto"): Busca una variable de entorno en tu sistema/Docker. 
Si existe, usa su valor; si no existe, toma el valor por defecto que le hemos puesto entre comillas. 
Esto evita poner la contraseña hardcodeada en el código."""

DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
"""DATABASE_URL: Construye la cadena de conexión (URI)
 que entiende PostgreSQL utilizando las variables anteriores: 
postgresql://usuario:contraseña@servidor:puerto/nombre_bd"""


def get_engine():
    return create_engine(DB_URL)
"""def get_engine():: Define la función que crea y devuelve el objeto engine.
return create_engine(DATABASE_URL): Instancia 
el motor de SQLAlchemy listo para ser utilizado por Pandas o cualquier consulta SQL."""