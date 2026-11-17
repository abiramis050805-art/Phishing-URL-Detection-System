# Phishing URL Detection System

## Project Overview

The Phishing URL Detection System is a machine learning-based cybersecurity project designed to identify suspicious URLs and classify them as legitimate or phishing.

The system uses URL-based feature extraction and a Random Forest Classifier to predict the category of a given website URL.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Random Forest Algorithm

## Dataset

- Dataset: PhiUSIIL Phishing URL Dataset
- Source: UCI Machine Learning Repository
- Total Records: 235,795
- Legitimate URLs: 134,850
- Phishing URLs: 100,945

## Features Extracted

The system extracts 11 URL-based features:

1. URL Length
2. Domain Length
3. HTTPS Status
4. IP Address Detection
5. Number of Dots
6. Number of Hyphens
7. Number of Digits
8. Number of Special Characters
9. Presence of @ Symbol
10. Suspicious Word Detection
11. Number of Subdomains

## Machine Learning Model

The project uses the Random Forest Classifier to classify URLs into two categories:

- 0 – Legitimate
- 1 – Phishing

## Model Performance

- Random train-test split accuracy: 99.56%
- Unseen-hostname evaluation accuracy: 99.54%

These results are based on the current dataset and evaluation setup. They do not guarantee the same performance on real-world URLs.

## Web Application

The Flask web interface allows users to:

- Enter a website URL.
- Scan the URL using the trained model.
- View the predicted category.
- View model confidence.
- See the extracted URL features.

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required libraries:

   `pip install flask pandas numpy scikit-learn`

4. Run the application:

   `python app.py`

5. Open your browser and visit:

   `http://127.0.0.1:5001`

## Project Structure

```text
Phishing URL Detection System/
│
├── dataset/
├── templates/
│   └── index.html
│
├── app.py
├── feature_extraction.py
├── phishing_model.pkl
├── train_improved_model.py
├── predict.py
├── evaluate_unseen_domains.py
└── README.md
```

## Disclaimer

This project is developed for educational and cybersecurity learning purposes. Predictions are based on URL features and should not be treated as a guarantee that a website is safe or malicious.