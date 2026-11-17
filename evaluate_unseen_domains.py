import pandas as pd
from urllib.parse import urlparse

from sklearn.model_selection import GroupShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Loading datasets...")

data = pd.read_csv("dataset/improved_url_dataset.csv")
original = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset.csv")

# Extract domain names for grouping
def get_domain(url):
    parsed = urlparse(str(url))
    domain = (parsed.hostname or "").lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain

groups = original["URL"].apply(get_domain)

# Separate features and labels
X = data.drop("label", axis=1)
y = data["label"]

# Split by domain, not by individual URL
splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.2,
    random_state=42
)

train_index, test_index = next(
    splitter.split(X, y, groups=groups)
)

X_train = X.iloc[train_index]
X_test = X.iloc[test_index]

y_train = y.iloc[train_index]
y_test = y.iloc[test_index]

print("\nDOMAIN-BASED DATA SPLIT")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print("Training domains:", groups.iloc[train_index].nunique())
print("Testing domains:", groups.iloc[test_index].nunique())

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

print("\nTraining model on known domains...")
model.fit(X_train, y_train)

# Evaluate on unseen domains
y_pred = model.predict(X_test)

print("\nUNSEEN DOMAIN EVALUATION")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Legitimate", "Phishing"],
    zero_division=0
))