from featureform import Client

# Initialize the client
client = Client(insecure=True)

# Try to access the feature
try:
    # List all available features
    print("Available features:")
    # Try to get the specific feature
    print("\nTrying to access User.avg_transactions:quickstart")
    result = client.features(
        [("avg_transactions", "quickstart")],
        {"user": "C2421688"}
    )
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}") 