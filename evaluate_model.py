import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv("dataset/phishing_dataset.csv")


# Feature extraction
def extract_features(url):

    return {
        "url_length": len(url),
        "has_https": int(url.startswith("https://")),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "digit_count": sum(char.isdigit() for char in url),
        "has_at_symbol": int("@" in url),
        "has_ip_address": int(
            any(part.isdigit() for part in url.split("/")[2].split("."))
            if "://" in url else False
        )
    }


# Convert URLs into numerical features
X = pd.DataFrame(
    data["url"].apply(extract_features).tolist()
)

# Classification labels
y = data["label"]


# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model using training data
model.fit(X_train, y_train)

# Predict testing data
y_pred = model.predict(X_test)


# Evaluate performance
print("MODEL EVALUATION RESULTS")

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Legitimate", "Phishing"],
    zero_division=0
))