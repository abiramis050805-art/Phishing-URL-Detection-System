import pandas as pd

data = pd.read_csv("dataset/cleaned_phishing_dataset.csv")

google_features = {
    "URLLength": 22,
    "DomainLength": 14,
    "IsDomainIP": 0,
    "NoOfQMarkInURL": 0,
    "NoOfAmpersandInURL": 0,
    "IsHTTPS": 1
}

conditions = True

for feature, value in google_features.items():
    conditions = conditions & (data[feature] == value)

matches = data[conditions]

print("GOOGLE FEATURE MATCHING RESULTS")
print("Total matching records:", len(matches))

if len(matches) > 0:
    print("\nLabel distribution:")
    print(matches["label"].value_counts())

    print("\nMatching URLs:")
    print(matches[["URL", "label"]].head(10))
else:
    print("No exact matching records found.")