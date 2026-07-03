import os
import feedparser
import requests

RSS_URL = os.getenv("RSS_URL")
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT")

if not RSS_URL:
    raise Exception("RSS_URL secret not found!")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN secret not found!")

if not CHAT_ID:
    raise Exception("TELEGRAM_CHAT secret not found!")

feed = feedparser.parse(RSS_URL)

if len(feed.entries) == 0:
    print("No posts found in RSS feed.")
    exit()

latest = feed.entries[0]

title = latest.title
link = latest.link

message = f"""📰 {title}

📖 বিস্তারিত পড়ুন:
{link}
"""

api = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    api,
    data={
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": False
    }
)

print(response.text)

if response.status_code == 200:
    print("Telegram post sent successfully.")
else:
    print("Failed to send Telegram message.")
