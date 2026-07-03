import os
import feedparser
import requests

RSS_URL = os.getenv("RSS_URL")
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT")

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("No posts found.")
    exit()

post = feed.entries[0]

title = post.title
link = post.link

message = f"""📰 {title}

📖 Read More:
{link}
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print(response.text)
