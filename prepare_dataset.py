import pandas as pd

# Load the original dataset
data = pd.read_csv(
    "dataset/PhiUSIIL_Phishing_URL_Dataset.csv"
)

# Select useful URL-related features
selected_columns = [
    "URL",
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "IsHTTPS",
    "HasPasswordField",
    "label"
]

# Create a new dataset
clean_data = data[selected_columns].copy()

# Convert labels to our project convention
# Original 1 = Legitimate, 0 = Phishing
# Project 0 = Legitimate, 1 = Phishing
clean_data["label"] = 1 - clean_data["label"]

# Save the prepared dataset
clean_data.to_csv(
    "dataset/cleaned_phishing_dataset.csv",
    index=False
)

print("DATASET PREPARED SUCCESSFULLY!")

print("\nNew Dataset Shape:")
print(clean_data.shape)

print("\nNew Label Distribution:")
print(clean_data["label"].value_counts())

print("\nFirst Five Records:")
print(clean_data.head())