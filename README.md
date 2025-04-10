# Feature Form Sample Project

This repository contains a sample project demonstrating the usage of Featureform for feature engineering and serving.

## Table of Contents
- [Installation](#installation)
- [Storage Layer](#storage-layer)
  - [PostgreSQL](#postgresql)
  - [Redis Inference Store](#inference-store-redis)
- [Usage Examples](#usage-examples)

## Installation

To install Featureform, follow the instructions in the [official documentation](https://docs.featureform.com/deployment/quickstart-docker#step-5%3A-dashboard-and-serving).

## Storage Layer

### PostgreSQL

PostgreSQL serves as the primary storage for raw data and transformations.

#### Connection

To connect to the PostgreSQL database running inside Docker:

```bash
PGPASSWORD="password" psql -h localhost -p 5432 -U postgres -d postgres
```

#### Useful Commands

- List all tables: `\dt`
- Transformations are persisted as tables with names like: `featureform_transformation__average_user_transaction__2025-04-0`

#### Sample Data

**Transactions Table:**
```sql
SELECT * FROM transactions LIMIT 1;
```
| transactionid | customerid | customerdob | custlocation | custaccountbalance | transactionamount | timestamp | isfraud |
|--------------|------------|-------------|--------------|-------------------|------------------|-----------|---------|
| T1 | C5841053 | 10/1/94 | JAMSHEDPUR | 17819.05 | 25 | 2022-04-09 11:33:09+00 | f |

**Transformation Result:**
```sql
SELECT * FROM "featureform_transformation__average_user_transaction__2025-04-0";
```
| user_id | avg_transaction_amt |
|---------|-------------------|
| C2421688 | 650 |

### Inference Store: Redis

Redis serves as the fast inference store for feature serving.

#### Connection

To connect to Redis running inside Featureform Docker:

```bash
redis-cli -h 127.0.0.1 -p 6379
```

#### Data Structure

1. **List all keys:**
```bash
keys *
```
Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "Featureform_table____tables"
```

2. **Get table metadata:**
```bash
hgetall Featureform_table____tables
```
Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "{\"ValueType\":\"float32\"}"
```

3. **Get feature value for a specific user:**
```bash
hget "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}" "C8029825"
```

## Usage Examples

### Feature Serving

```python
from featureform import Client

# Initialize the client
client = Client(insecure=True)

# Get feature value for a specific user
result = client.features(
    [("avg_transactions", "quickstart")],
    {"user": "C2421688"}
)
print(f"Result: {result}")
```

### Training Set Access

```python
from featureform import Client

client = Client(insecure=True)
ts_name = "fraud_training"
ts_variant = "quickstart"

dataset = client.training_set(ts_name, ts_variant)
for batch in dataset:
    print(batch)
```

### API Server

The project includes a Flask API server for serving features:

```python
from flask import Flask, jsonify
from featureform import Client

app = Flask(__name__)
serving = Client(insecure=True)

@app.route('/feature/<user_id>', methods=['GET'])
def get_user_feature(user_id):
    try:
        user_feat = serving.features(
            [("avg_transactions", "quickstart")], 
            {"user": user_id}
        )
        return jsonify({
            "user_id": user_id,
            "feature_value": user_feat
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

## Contributing

Feel free to submit issues and enhancement requests!

