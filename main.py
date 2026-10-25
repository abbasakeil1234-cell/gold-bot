import os
import time
import requests

TOKEN = "8325883841:AAElTRH4Sv7c0eFMxFgkib6ebC7B6xzEGgk"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    try:
        requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": text})
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Gold Bot is running 24/7...")
    offset = None
    while True:
        try:
            res = requests.get(URL + "getUpdates", params={"offset": offset, "timeout": 30})
            data = res.json()
            if "result" in data:
                for update in data["result"]:
                    offset = update["update_id"] + 1
                    if "message" in update:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"].get("text", "")
                        if text == "/start":
                            send_message(chat_id, "أهلاً بك! بوت تحليل الذهب XAUUSD يعمل الآن بنجاح 24/7 🚀")
        except Exception as e:
            print(f"Connection error: {e}")
            time.sleep(5)
        time.sleep(1)

if __name__ == "__main__":
    main()
