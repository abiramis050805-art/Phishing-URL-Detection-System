import pandas as pd
from feature_extraction import extract_features

print("Loading original dataset...")

data = pd.read_csv(
    "dataset/PhiUSIIL_Phishing_URL_Dataset.csv"
)

print("Extracting URL features...")

feature_data = data["URL"].apply(extract_features)

features_df = pd.DataFrame(feature_data.tolist())

# Convert labels: 1 = phishing, 0 = legitimate
features_df["label"] = 1 - data["label"]

# Save the new dataset
features_df.to_csv(
    "dataset/improved_url_dataset.csv",
    index=False
)

print("\nIMPROVED DATASET CREATED!")
print("Dataset shape:", features_df.shape)

print("\nLabel distribution:")
print(features_df["label"].value_counts())

print("\nFirst five records:")
print(features_df.head())