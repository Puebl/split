import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
if not TELEGRAM_BOT_TOKEN:
    print("[WARN] TELEGRAM_BOT_TOKEN is empty. Set it in .env before running the bot.")
