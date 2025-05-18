from pymongo.mongo_client import MongoClient
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# MongoDB Connection
uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['inventory']
collection = db['supplychain_data']

# Read data
data = list(collection.find())
df = pd.DataFrame(data).drop(columns=["_id"])

# Spark Session
spark = SparkSession.builder.appName("Supply Chain Inventory Cost Prediction").getOrCreate()
inventory_df = spark.createDataFrame(df)

# Feature Engineering
assembler = VectorAssembler(inputCols=["Price", "Stock levels"], outputCol="features")
data = assembler.transform(inventory_df).select("features", "price")

# Train-Test Split
train_data, test_data = data.randomSplit([0.8, 0.2])

# Model Training
rf = RandomForestRegressor(featuresCol="features", labelCol="price", numTrees=100)
model = rf.fit(train_data)

# Prediction
prediction = model.transform(test_data)

# Evaluation
evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(prediction)
print(f"Root Mean Squared Error: {rmse}")

# Save prediction to MongoDB
df_prediction = prediction.select("price", "prediction").toPandas()
collection_prediction = db['prediction_data']
collection_prediction.insert_many(df_prediction.to_dict(orient="records"))
