# 🔍 Port Scanner + Threat Intelligence Lookup (GUI Web App)

This is a Python-based cybersecurity tool that allows you to:
- Scan common ports of one or more IP addresses
- Get threat intelligence data from AbuseIPDB
- View GeoIP and risk levels
- Export results as a CSV report
- Use it through a simple **Streamlit Web GUI**

## 🚀 Live Demo

🟢 **Try the app online here** (hosted via Streamlit Cloud):  
[👉 Click to open the Web App](https://port-scanner-threat-intel-nh9ewu6rheokuygklubn5b.streamlit.app/).

## 🎯 Features

- ✅ Quick port scanning of multiple IPs
- ✅ Threat score lookup using [AbuseIPDB](https://abuseipdb.com/)
- ✅ GeoIP country/usage detection
- ✅ Risk level color-coded (Low / Medium / High)
- ✅ Export scan results to CSV
- ✅ Simple Web GUI with [Streamlit](https://streamlit.io/)

---

## 📁 Folder Structure

📁 project/
│
├── gui_app.py # Main Streamlit app
├── scanner.py # Port scanning functions
├── threat_lookup.py # Threat & geo info functions
├── utils.py # Risk rating, export, logging
├── requirements.txt # All required Python packages
├── ip_list.txt # Sample IPs to scan (optional)
├── .gitignore # Prevents secret/key files upload


🛡️ Notes & Warnings
This tool is for educational and defensive use only.
Do not use it to scan IPs you don’t own or don’t have permission to scan.
AbuseIPDB has a free tier with usage limits.

🧠 About
This project was built to practice:
Python networking
Cybersecurity fundamentals
Threat Intelligence integration
GUI app development with Streamlit

📃 License
This project is released under the MIT License
