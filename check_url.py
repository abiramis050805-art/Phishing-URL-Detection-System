import pandas as pd

data = pd.read_csv(
    "dataset/cleaned_phishing_dataset.csv"
)

# Show 5 legitimate examples
print("LEGITIMATE URL EXAMPLES")

print(
    data[data["label"] == 0][
        ["URL"] + [
            col for col in data.columns
            if col not in ["URL", "label"]
        ]
    ].head(5).to_string(index=False)
)

# Show 5 phishing examples
print("\nPHISHING URL EXAMPLES")

print(
    data[data["label"] == 1][
        ["URL"] + [
            col for col in data.columns
            if col not in ["URL", "label"]
        ]
    ].head(5).to_string(index=False)
)