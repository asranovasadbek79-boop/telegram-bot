import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def main():
bot = Bot(token=TOKEN)

```
accounts = [
    ("🎮 PUBG AKKAUNT №1", "🟢 BO‘SH"),
    ("🎮 PUBG AKKAUNT №2", "🔴 BAND"),
    ("🎮 PUBG AKKAUNT №3", "🟢 BO‘SH"),
]

text = "🔥 PUBG AKKAUNT IJARASI 🔥\n\n"

for name, status in accounts:
    text += f"{name}\nHolati: {status}\n\n"

text += "📩 Ijara uchun admin bilan bog‘laning!"

await bot.send_message(chat_id=CHANNEL_ID, text=text)
```

if **name** == "**main**":
import asyncio
asyncio.run(main())
