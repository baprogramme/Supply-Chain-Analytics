## 📥 Step 1: Data Ingestion to MongoDB

Install required libraries:

```bash
pip install pymongo --upgrade pip

from pymongo.mongo_client import MongoClient
import pandas as pd

uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['inventory']
collection = db['supplychain_data']

# Load CSV
df = pd.read_csv('supply_chain_data.csv')
data_dict = df.to_dict(orient='records')
collection.insert_many(data_dict)

print(f"Successfully inserted {len(data_dict)} records.")
client.close()
