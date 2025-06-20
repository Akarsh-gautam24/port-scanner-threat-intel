from datetime import datetime
import pandas as pd

def rate_risk(score):
    if score >= 70:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"

def log_result(ip, ports, threat_info):
    with open("scan_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] {ip} | Ports: {ports} | Abuse Score: {threat_info.get('abuse_score')}\n")

def export_csv(results):
    df = pd.DataFrame(results)
    df.to_csv("scan_results.csv", index=False)
