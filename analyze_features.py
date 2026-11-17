import pandas as pd

data = pd.read_csv(
    "dataset/cleaned_phishing_dataset.csv"
)

print("HTTPS DISTRIBUTION BY CLASS")

print(
    pd.crosstab(
        data["IsHTTPS"],
        data["label"],
        normalize="index"
    ).round(4)
)

print("\nAVERAGE FEATURE VALUES")

print(
    data.groupby("label")[
        [
            "URLLength",
            "DomainLength",
            "IsDomainIP",
            "NoOfQMarkInURL",
            "NoOfAmpersandInURL",
            "IsHTTPS"
        ]
    ].mean().round(2)
)

print("\nGOOGLE FEATURE VALUES")

google = pd.DataFrame([{
    "URLLength": 22,
    "DomainLength": 14,
    "IsDomainIP": 0,
    "NoOfQMarkInURL": 0,
    "NoOfAmpersandInURL": 0,
    "IsHTTPS": 1
}])

print(google)