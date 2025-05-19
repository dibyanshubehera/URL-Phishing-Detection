from flask import Flask, render_template, request
import re, socket, whois 
from datetime import datetime
import tldextract

app = Flask(__name__)
 
 
def has_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return re.match(r"\d+\.\d+\.\d+\.\d+", ip) is not None
    except:
        return False

def domain_age(domain):
    try:
        info = whois.whois(domain)
        creation_date = info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        return (datetime.now() - creation_date).days
    except:
        return 0

def extract_features(url):
    features = {}
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}"

    features["long_url"] = len(url) > 75
    features["ip_address"] = has_ip(ext.domain)
    features["has_at"] = "@" in url
    features["has_hyphen"] = "-" in ext.domain
    features["many_subdomains"] = len(ext.subdomain.split(".")) > 2
    features["has_https"] = url.startswith("https://")
    features["domain_young"] = domain_age(domain) < 180
    features["https_in_domain"] = "https" in ext.domain

    return features

def predict(features):
    score = sum(features.values())
    return "Phishing" if score >= 3 else "Legitimate"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    features = {}
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        result = predict(features)
    return render_template("index.html", result=result, features=features)

if __name__ == "_main_":
    app.run(debug=True)