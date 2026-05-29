from pyspark.sql.functions import col

def build_features(df):
    df = df.drop("RowNumber", "CustomerId", "Surname")

    df = df.withColumn(
        "BalanceSalaryRatio",
        col("Balance") / (col("EstimatedSalary") + 1)
    )

    return df