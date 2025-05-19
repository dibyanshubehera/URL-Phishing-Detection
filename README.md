
This is a cybersecurity project that detects phishing URLs using a *rule-based approach*. It analyzes different features of a URL—such as its length, the presence of special characters, use of IP addresses, and suspicious keywords—to determine whether the URL is legitimate or potentially malicious.

This project is intended as a lightweight, explainable alternative to machine learning methods.

# Features
- Detects phishing URLs using predefined rules
- Fast, simple, and easy to understand
- No training data or machine learning required
- Suitable for educational and small-scale security use cases

# Technologies Used
- Python 3
- Regular Expressions (re)
- pandas (for reading and analyzing URL datasets, if used)

# Rule-Based Detection Logic
The program checks for:
- Use of IP addresses instead of domain names
- Suspicious characters (like @, -, //)
- Long URL lengths
- Use of HTTPS vs HTTP
- Presence of misleading keywords (e.g., "login", "verify", "secure")

# How to Run

1. *Clone the Repository*
   ```bash
   git clone https://github.com/dibyanshubehera/url-phishing-detection.git
   cd url-phishing-detection