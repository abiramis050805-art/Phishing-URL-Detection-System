import pickle
import pandas as pd

from feature_extraction import extract_features

# Load trained model
with open("phishing_model.pkl", "rb") as file:
    saved_data = pickle.load(file)

model = saved_data["model"]
features = saved_data["features"]

print("PHISHING URL DETECTION SYSTEM")
print("-" * 40)

url = input("Enter a URL: ")

# Extract URL features
extracted_features = extract_features(url)

input_data = pd.DataFrame(
    [extracted_features]
)[features]

print("\nEXTRACTED FEATURES")
print(input_data.to_string(index=False))

# Predict
prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]

print("\nPREDICTION PROBABILITIES")
print("Legitimate:", round(probabilities[0] * 100, 2), "%")
print("Phishing:", round(probabilities[1] * 100, 2), "%")

print("\nPREDICTION RESULT")

if prediction == 1:
    print("WARNING! This URL is predicted as PHISHING.")
else:
    print("This URL is predicted as LEGITIMATE.")

print("\nNote: This prediction is not a guarantee of website safety.")