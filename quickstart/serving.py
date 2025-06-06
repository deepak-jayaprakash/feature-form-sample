from featureform import Client

serving = Client(insecure=True)

transformation_name = "avg_transactions"
transformation_variant = "quickstart"

user_feat = serving.features(
    [(transformation_name, transformation_variant)], 
    {"user": "C2421688"}
)
user_feat_sum = serving.features(
    [("sum_transactions", "quickstart2")], 
    {"user": "C2421688"}
)
print(f"User Result: {user_feat}")
print(f"User Result Sum: {user_feat_sum}")
