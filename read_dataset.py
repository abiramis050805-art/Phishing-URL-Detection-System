import pandas as pd

# Load the dataset
data = pd.read_csv("dataset/phishing_dataset.csv")

# Display the dataset
print(data)

# Display first five records
print("\nFirst five records:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Count legitimate and phishing URLs
print("\nURL Classification:")
print(data["label"].value_counts())