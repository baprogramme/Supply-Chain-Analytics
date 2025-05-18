# 📦 Supply Chain Analytics
End-to-end Supply Chain Cost Prediction using MongoDB, Python &amp; Spark

This project demonstrates an end-to-end pipeline for ingesting supply chain data, processing it with Spark, predicting product costs using machine learning, and saving the predictions back to MongoDB.

---

## 🚀 Overview

- **Source**: Supply Chain data from a CSV file.
- **Storage**: MongoDB (`inventory` database, `supplychain_data` collection).
- **Processing & Prediction**: Apache Spark and MLlib in Databricks.
- **Output**: Predicted cost values stored in MongoDB (`prediction_data` collection).

---

## 🧰 Tools & Technologies

- Python
- MongoDB (using `pymongo`)
- Apache Spark (in Databricks)
- MLlib (Random Forest Regression)
- Pandas
- PySpark

---

## 🗂️ Project Structure

```
supply-chain-analytics/
│
├── supply_chain_data.csv # Raw supply chain data file
│
├── data_ingestion.py # Python script to ingest data into MongoDB
│
├── cost_prediction_spark.py # Spark code for cost prediction using ML
│
└── README.md  # Project documentation
```
