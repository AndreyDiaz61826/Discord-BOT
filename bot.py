import os
import requests

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

def send(message):
    requests.post(WEBHOOK_URL, json={"content": message})

for p in products:
    if p["status"] == "new":
        msg = f"""
━━━━━━━━━━━━━━━
🛒 MEDIA SHOP

📦 {p['name']}
💰 {p['price']}

{p['desc']}

📩 Заказ: создайте Issue или напишите в ЛС
━━━━━━━━━━━━━━━
"""
        send(msg)
