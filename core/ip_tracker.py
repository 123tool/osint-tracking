import json
import requests
import time
from core.banner import Wh, Cy, Re, Ye, display_ip_banner, display_myip_banner

def track_target_ip():
    display_ip_banner()
    try:
        ip = input(f"{Wh}\n Enter Target IP : {Cy}")
        print()
        print(f' {Wh}============= {Cy}METADATA TARGET GEOLOCATION IP {Wh}=============')
        req_api = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        ip_data = json.loads(req_api.text)
        time.sleep(1)
        
        if ip_data.get("success"):
            print(f"{Wh}\n IP Target       :{Cy}", ip)
            print(f"{Wh} Type IP         :{Cy}", ip_data.get("type"))
            print(f"{Wh} Country         :{Cy}", ip_data.get("country"))
            print(f"{Wh} Country Code    :{Cy}", ip_data.get("country_code"))
            print(f"{Wh} City            :{Cy}", ip_data.get("city"))
            print(f"{Wh} Continent       :{Cy}", ip_data.get("continent"))
            print(f"{Wh} Region          :{Cy}", ip_data.get("region"))
            print(f"{Wh} Region Code     :{Cy}", ip_data.get("region_code"))
            print(f"{Wh} Latitude        :{Cy}", ip_data.get("latitude"))
            print(f"{Wh} Longitude       :{Cy}", ip_data.get("longitude"))
            
            lat = ip_data.get('latitude', 0)
            lon = ip_data.get('longitude', 0)
            print(f"{Wh} Maps Targeting  :{Cy}", f"https://www.google.com/maps/@{lat},{lon},10z")
            print(f"{Wh} Postal Code     :{Cy}", ip_data.get("postal"))
            print(f"{Wh} Calling Code    :{Cy}", ip_data.get("calling_code"))
            print(f"{Wh} Capital City    :{Cy}", ip_data.get("capital"))
            print(f"{Wh} ASN Connection  :{Cy}", ip_data.get("connection", {}).get("asn"))
            print(f"{Wh} ISP Owner       :{Cy}", ip_data.get("connection", {}).get("isp"))
            print(f"{Wh} Domain Routing  :{Cy}", ip_data.get("connection", {}).get("domain"))
            print(f"{Wh} Timezone ID     :{Cy}", ip_data.get("timezone", {}).get("id"))
            print(f"{Wh} System Time     :{Cy}", ip_data.get("timezone", {}).get("current_time"))
        else:
            print(f" {Re}[!] Failed to gather information. Invalid IP Address.")
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROCESS TERMINATED BY USER...")
    except Exception as e:
        print(f" {Re}[!] Connection Error: {str(e)}")

def track_self_ip():
    display_myip_banner()
    try:
        print(f"\n {Wh}========== {Cy}GATHERING CURRENT HOST INTERNET PROFILE {Wh}==========")
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        public_ip = response.json()['ip']
        
        req_details = requests.get(f"http://ipwho.is/{public_ip}", timeout=10).json()
        
        print(f"\n {Wh}[+] Public IP Detected : {Cy}{public_ip}")
        print(f" {Wh}[+] Local Provider/ISP : {Cy}{req_details.get('connection', {}).get('isp')}")
        print(f" {Wh}[+] Current Gateway    : {Cy}{req_details.get('connection', {}).get('org')}")
        print(f" {Wh}[+] Regional Sector    : {Cy}{req_details.get('city')}, {req_details.get('country')}")
        print(f"\n {Wh}======================================================")
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROCESS TERMINATED...")
    except Exception as e:
        print(f" {Re}[!] Failed to reach verification servers: {str(e)}")
