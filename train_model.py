import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv(
    "dataset/cleaned_phishing_dataset.csv"
)

# Select only URL-based features
features = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "IsHTTPS"
]

X = data[features]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train
print("Training URL-only model...")
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

print("\nMODEL EVALUATION")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Legitimate", "Phishing"]
    )
)

# Save model and feature names
with open("phishing_model.pkl", "wb") as file:
    pickle.dump(
        {
            "model": model,
            "features": features
        },
        file
    )

print("\nURL-only model saved successfully!")