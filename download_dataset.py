import pandas as pd
from ucimlrepo import fetch_ucirepo

print("Downloading phishing dataset...")

# Fetch dataset from UCI
dataset = fetch_ucirepo(id=967)

# Get URL and target columns
urls = dataset.data.features["URL"]
labels = dataset.data.targets["label"]

# Create a clean dataset
data = pd.DataFrame({
    "url": urls,
    "label": (labels == 0).astype(int)
})

# Remove missing and duplicate URLs
data = data.dropna()
data = data.drop_duplicates(subset="url")

# Save dataset
data.to_csv(
    "dataset/phishing_dataset.csv",
    index=False
)

print("\nDataset downloaded successfully!")
print("Total records:", len(data))
print("\nLabel distribution:")
print(data["label"].value_counts())

print("\nDataset saved successfully!")