import streamlit as st
from scanner import scan_ports
from threat_lookup import abuseipdb_lookup, geoip_lookup
from utils import rate_risk, export_csv
from dotenv import load_dotenv
import os
import time

# Load API key
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

st.set_page_config(page_title="Threat Intel Port Scanner", layout="centered")
st.title("🔍 Port Scanner + Threat Intelligence Tool")

st.markdown("Enter IP address(es) to scan below. You can also upload a file containing multiple IPs.")

# Input for single IP or list
ip_input = st.text_area("📥 Enter IP(s):", placeholder="Example:\n8.8.8.8\n1.1.1.1")
uploaded_file = st.file_uploader("📁 Or upload a file with IPs (one per line)", type=["txt"])

scan_button = st.button("🚀 Start Scan")

if scan_button:
    st.info("⏳ Scanning in progress... please wait.")
    ips = []

    if ip_input.strip():
        ips += [line.strip() for line in ip_input.strip().splitlines() if line.strip()]
    
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8").splitlines()
        ips += [line.strip() for line in file_content if line.strip()]

    if not ips:
        st.error("❌ Please enter or upload at least one IP address.")
    else:
        results = []
        for ip in ips:
            st.write(f"🔎 Scanning: {ip}")
            start_time = time.time()
            common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 8080]
            open_ports = scan_ports(ip, common_ports)
            threat_info = abuseipdb_lookup(ip, API_KEY)
            geo_info = geoip_lookup(ip)

            abuse_score = threat_info.get("abuse_score", 0)
            risk = rate_risk(abuse_score)
            duration = round(time.time() - start_time, 2)

            result = {
                "IP": ip,
                "Open Ports": ', '.join(map(str, open_ports)) if open_ports else "None",
                "Abuse Score": abuse_score,
                "Risk Level": risk,
                "Country": threat_info.get("country", geo_info.get("country", "Unknown")),
                "Usage Type": threat_info.get("usage_type", "Unknown"),
                "Scan Time (s)": duration
            }

            results.append(result)

        if results:
            st.success("✅ Scan completed.")
            st.dataframe(results)

            # Save to CSV and offer download
            export_csv(results)
            with open("scan_results.csv", "rb") as file:
                st.download_button("⬇️ Download CSV", file, file_name="scan_results.csv")

