from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('streetwearanalytics').getOrCreate()

path = 'data/output/silver'

df = (
    spark.read
    .parquet(path)
) 

df_category_metrics = (
    df
    .groupBy('category_name')
    .agg(
        F.count('product_id').alias('total_products'),
        F.round(F.avg('price'),2).alias('avg_price'),
        F.max('price').alias('max_price')
    ).orderBy(F.col('avg_price').desc())
)

df_tier_metrics = (
    df
    .groupBy('price_tier')
    .agg(
        F.count('product_id').alias('total_products'),
        F.round(F.avg('price_with_vat'),2).alias('avg_price_vat')
    ).orderBy(F.desc('total_products'))
)

#definimos el partition by y orden 1 vez, de esta forma no lo repetiremos mas veces
#usando esta variable
window_spec = Window.partitionBy('category_name').orderBy(F.desc('price'))

df_ranked_products = (
    df
    .withColumn(
        'price_rank',
        F.dense_rank().over(window_spec)
    )
    .where(F.col('price_rank') <= 3)
    .select('category_name', 'price_rank', 'product_name', 'price')
    .orderBy('category_name', 'price_rank')   
)


print("\n=== TOP 3 PRODUCTOS MÁS CAROS POR CATEGORÍA ===")
df_ranked_products.show(truncate=False)

# ==========================================
# 3. CARGA / PERSISTENCIA (CAPA GOLD)
# ==========================================
gold_base_path = 'data/output/gold'
Path(gold_base_path).mkdir(parents=True, exist_ok=True)

# 1. Métricas por categoría
(
    df_category_metrics
    .write
    .mode("overwrite")
    .parquet(f"{gold_base_path}/category_metrics")
)

# 2. Métricas por rango de precio
(
    df_tier_metrics
    .write
    .mode("overwrite")
    .parquet(f"{gold_base_path}/tier_metrics")
)

# 3. Ranking de productos más caros
(
    df_ranked_products
    .write
    .mode("overwrite")
    .parquet(f"{gold_base_path}/ranked_products")
)

print(f"\n[OK] Capa Gold persistida correctamente en {gold_base_path}/")

# ==========================================
# 4. CIERRE DE SESIÓN
# ==========================================
spark.stop()