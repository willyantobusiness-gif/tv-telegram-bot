from flask import Flask, request
import requests

BOT_TOKEN = "8582615236:AAFgWcmZ02r9mCWgtgQu7s9gLZ1gIIETjME"
CHAT_ID = "8563927232"

app = Flask(__name__)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    msg = f"""
📢 <b>TRADINGVIEW ALERT</b>

📊 Pair : {data.get('symbol')}
📌 Signal : {data.get('signal')}
💰 Price : {data.get('price')}
⏰ TF : {data.get('timeframe')}
🕒 Time : {data.get('time')}
"""
    send_telegram(msg)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

