# Feature Form Sample Project

This repository contains a sample project demonstrating the usage of Featureform for feature engineering and serving.

## Installation

To install Featureform, follow the instructions in the [official documentation](https://docs.featureform.com/deployment/quickstart-docker#step-5%3A-dashboard-and-serving).

## Storage Layer

### PostgreSQL

To connect to the PostgreSQL database running inside Docker:

```bash
PGPASSWORD="password" psql -h localhost -p 5432 -U postgres -d postgres
```

#### Useful Commands

- List all tables: `\dt`
- Transformations are persisted as tables with names like: `featureform_transformation__average_user_transaction__2025-04-0`

#### Sample Transformations Data

```sql
SELECT * FROM "featureform_transformation__average_user_transaction__2025-04-0";
```

| user_id  | avg_transaction_amt |
|----------|---------------------|
| C2421688 | 650                 |

### Inference Store: Redis

To connect to Redis running inside Featureform Docker:

```bash
redis-cli -h 127.0.0.1 -p 6379
```

#### Sample Inference Data

List all keys:
```
keys *
```

Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "Featureform_table____tables"
```

Get table metadata:
```
hgetall Featureform_table____tables
```

Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "{\"ValueType\":\"float32\"}"
```

Get feature value for a specific user:
```
hget "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}" "C8029825"
```

Example output:
```
"150"
```

