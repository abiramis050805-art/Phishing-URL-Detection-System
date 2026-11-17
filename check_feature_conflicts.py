import pandas as pd

data = pd.read_csv("dataset/cleaned_phishing_dataset.csv")

features = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "IsHTTPS"
]

groups = data.groupby(features)["label"].nunique()

conflicts = groups[groups > 1]

print("FEATURE COMBINATION ANALYSIS")
print("Total unique feature combinations:", len(groups))
print("Conflicting combinations:", len(conflicts))

print("\nLabel distribution for Google's feature combination:")

google = data[
    (data["URLLength"] == 22) &
    (data["DomainLength"] == 14) &
    (data["IsDomainIP"] == 0) &
    (data["NoOfQMarkInURL"] == 0) &
    (data["NoOfAmpersandInURL"] == 0) &
    (data["IsHTTPS"] == 1)
]

print(google["label"].value_counts())