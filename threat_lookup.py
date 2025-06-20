import requests

def abuseipdb_lookup(ip, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        data = response.json().get("data", {})
        return {
            "abuse_score": data.get("abuseConfidenceScore", 0),
            "country": data.get("countryCode", "Unknown"),
            "isp": data.get("isp", "Unknown"),
            "usage_type": data.get("usageType", "Unknown")
        }
    except Exception:
        return {
            "abuse_score": 0,
            "country": "Unknown",
            "usage_type": "Unknown"
        }

def geoip_lookup(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = res.json()
        return {
            "city": data.get("city", ""),
            "region": data.get("regionName", ""),
            "country": data.get("country", "Unknown"),
            "lat": data.get("lat", ""),
            "lon": data.get("lon", "")
        }
    except:
        return {"country": "Unknown"}
