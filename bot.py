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
