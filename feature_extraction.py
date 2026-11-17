from urllib.parse import urlparse
import ipaddress
import re

def extract_features(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed_url = urlparse(url)
    domain = parsed_url.hostname or ""

    # Check whether domain is an IP address
    try:
        ipaddress.ip_address(domain)
        is_ip = 1
    except ValueError:
        is_ip = 0

    # URL features
    features = {
        "URLLength": len(url),
        "DomainLength": len(domain),
        "IsHTTPS": 1 if parsed_url.scheme == "https" else 0,
        "IsDomainIP": is_ip,
        "NoOfDots": url.count("."),
        "NoOfHyphens": url.count("-"),
        "NoOfDigits": sum(char.isdigit() for char in url),
        "NoOfSpecialChars": len(re.findall(r'[^a-zA-Z0-9]', url)),
        "HasAtSymbol": 1 if "@" in url else 0,
        "HasSuspiciousWord": 1 if re.search(
            r'login|verify|update|account|secure|banking|signin',
            url,
            re.IGNORECASE
        ) else 0,
        "NoOfSubDomain": max(len(domain.split(".")) - 2, 0)
    }

    return features