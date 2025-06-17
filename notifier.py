import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("7683588656:AAFBuPRe0f6AQE_CJ0nkMHjwlhhYhu-29E4")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_CHAT_ID=7786909771")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_USER_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()
