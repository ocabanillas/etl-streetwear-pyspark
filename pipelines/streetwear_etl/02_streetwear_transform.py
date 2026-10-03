from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('streetwearjsonAPI').getOrCreate()

raw_path = 'data/raw/streetwear_products_raw.json'

df = (
    spark.read
    .option('multiline', 'true')
    .json(raw_path)
)
#multiline es para indicarle que en este caso la columna producto ocupa varias lienas fisicas

'''
|-- id: long
|-- title: string
|-- price: long
|-- category: struct #struct significa que el campo contiene un diccionario
|    |-- id: long
|    |-- name: string
|    |-- image: string
|-- images: array # array es una caja que contiene una cadena de strings
|    |-- element: string
'''

#convertimos los campos y aquellos struct que es un diccionario dentro de una celda
df_flat_category = df.select(
    F.col('id').alias('product_id'),
    F.col('title').alias('product_name'),
    F.col('price'),
    F.col('category.id').alias('category_id'),
    F.col('category.name').alias('category_name'),
    F.col('images')[0].alias('primary_image_url')

)

df_cleaned = (
    df_flat_category
    .withColumn(
        'product_name',
        F.trim(F.lower(F.col('product_name')))
    )
    .withColumn(
        'category_name',
        F.trim(F.lower(F.col('category_name')))
    )
    .where(
        (F.col('price') > 0) &
        (F.col('price').isNotNull()) &
        (F.col('product_name').isNotNull())
    )
)


df_calculated = (
    df_cleaned
    .withColumn(
        'price_with_vat',
        F.round((F.col('price') * 1.21),2)
    )
    .withColumn(
        'price_tier',
        F.when(F.col('price') < 30, F.lit('budget'))
        .when((F.col('price') >=30) & (F.col('price') <= 70), F.lit('Mid-range'))
        .otherwise(F.lit('premium'))
        )

    )

    
(
df_calculated
    .write
    .mode('overwrite')
    .partitionBy('category_name')
    .parquet('data/output/products_silver')
)
print(f"[SUCCESS] Transformación Silver completada con éxito. Registros procesados: {df_calculated.count()}")
