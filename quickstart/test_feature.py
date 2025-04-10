import featureform as ff
import sys
from typing import List, Dict, Any
from datetime import datetime

def initialize_client():
    """Initialize the Featureform client with insecure mode."""
    try:
        client = ff.Client(insecure=True)
        print("Featureform client initialized successfully")
        return client
    except Exception as e:
        print(f"Error initializing client: {str(e)}")
        sys.exit(1)

def list_features(client: ff.Client):
    """List all features registered in Featureform."""
    try:
        print("\nListing all features:")
        print("-" * 50)
        features = client.list_features()
        if not features:
            print("No features found")
            return
        
        for feature in features:
            print(f"Feature: {feature.name}")
            print(f"Variant: {feature.variant}")
            print(f"Type: {feature.type}")
            print(f"Entity: {feature.entity}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing features: {str(e)}")

def list_sources(client: ff.Client):
    """List all sources registered in Featureform."""
    try:
        print("\nListing all sources:")
        print("-" * 50)
        sources = client.list_sources()
        if not sources:
            print("No sources found")
            return
        
        for source in sources:
            print(f"Source: {source.name}")
            print(f"Variant: {source.variant}")
            print(f"Type: {source.type}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing sources: {str(e)}")

def list_labels(client: ff.Client):
    """List all labels registered in Featureform."""
    try:
        print("\nListing all labels:")
        print("-" * 50)
        labels = client.list_labels()
        if not labels:
            print("No labels found")
            return
        
        for label in labels:
            print(f"Label: {label.name}")
            print(f"Variant: {label.variant}")
            print(f"Type: {label.type}")
            print(f"Entity: {label.entity}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing labels: {str(e)}")

def list_training_sets(client: ff.Client):
    """List all training sets registered in Featureform."""
    try:
        print("\nListing all training sets:")
        print("-" * 50)
        training_sets = client.list_training_sets()
        if not training_sets:
            print("No training sets found")
            return
        
        for ts in training_sets:
            print(f"Training Set: {ts.name}")
            print(f"Variant: {ts.variant}")
            print(f"Label: {ts.label}")
            print(f"Features: {ts.features}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing training sets: {str(e)}")

def list_providers(client: ff.Client):
    """List all providers registered in Featureform."""
    try:
        print("\nListing all providers:")
        print("-" * 50)
        providers = client.list_providers()
        if not providers:
            print("No providers found")
            return
        
        for provider in providers:
            print(f"Provider: {provider.name}")
            print(f"Type: {provider.type}")
            print(f"Status: {provider.status}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing providers: {str(e)}")

def list_entities(client: ff.Client):
    """List all entities registered in Featureform."""
    try:
        print("\nListing all entities:")
        print("-" * 50)
        entities = client.list_entities()
        if not entities:
            print("No entities found")
            return
        
        for entity in entities:
            print(f"Entity: {entity.name}")
            print(f"Description: {entity.description}")
            print("-" * 30)
    except Exception as e:
        print(f"Error listing entities: {str(e)}")

def main():
    """Main function to run all listing commands."""
    client = initialize_client()
    
    # List all resources
    list_providers(client)
    list_entities(client)
    list_sources(client)
    list_features(client)
    list_labels(client)
    list_training_sets(client)

if __name__ == "__main__":
    main() 