import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USER_ID = os.getenv("TELEGRAM_USER_ID")

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        print(f"狀態碼: {response.status_code}")
        print(f"回應: {response.text}")
    except Exception as e:
        print("發送訊息失敗：", str(e))
