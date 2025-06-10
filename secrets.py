import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import Filters

BOT_TOKEN = "TOKEN"
DB_URI = "DATABAS_URL"
SUDO_USERS = 
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = -1002153866511
