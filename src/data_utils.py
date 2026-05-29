def read_csv(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)


def save_table(df, table_name):
    df.write.mode("overwrite").saveAsTable(table_name)