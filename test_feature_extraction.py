from feature_extraction import extract_features

# Test URLs
test_urls = [
    "https://www.google.com",
    "https://www.microsoft.com",
    "http://example.com/login/verify",
    "http://192.168.1.1/account"
]

for url in test_urls:
    print("\nURL:", url)
    print("-" * 50)

    features = extract_features(url)

    for feature, value in features.items():
        print(f"{feature}: {value}")