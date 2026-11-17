from flask import Flask, render_template, request
import pickle
import pandas as pd

from feature_extraction import extract_features

app = Flask(__name__)

# Load trained machine learning model
with open("phishing_model.pkl", "rb") as file:
    saved_data = pickle.load(file)

model = saved_data["model"]
features = saved_data["features"]


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    probability = None
    entered_url = ""
    error = None
    feature_details = None

    if request.method == "POST":

        entered_url = request.form.get("url", "").strip()

        # Basic URL validation
        if not entered_url:
            error = "Please enter a URL."

        elif "." not in entered_url:
            error = "Please enter a valid website URL."

        else:

            # Extract URL features
            extracted = extract_features(entered_url)

            feature_details = extracted

            # Prepare input for prediction
            input_data = pd.DataFrame(
                [extracted]
            )[features]

            # Predict URL category
            prediction = model.predict(input_data)[0]

            probabilities = model.predict_proba(input_data)[0]

            probability = round(
                max(probabilities) * 100, 2
            )

            if prediction == 1:
                result = "PHISHING"
            else:
                result = "LEGITIMATE"

    return render_template(
        "index.html",
        result=result,
        probability=probability,
        entered_url=entered_url,
        error=error,
        feature_details=feature_details
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)