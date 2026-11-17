import pandas as pd

# Load the original dataset
data = pd.read_csv(
    "dataset/PhiUSIIL_Phishing_URL_Dataset.csv"
)

# Display dataset details
print("DATASET LOADED SUCCESSFULLY!")

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns.tolist())

print("\nFirst Five Records:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Information:")
print(data.info())

print("\nLabel Distribution:")
print(data["label"].value_counts())

print("\nUnique Label Values:")
print(data["label"].unique())