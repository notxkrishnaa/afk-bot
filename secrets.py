import os

if not os.environ.get("TOKEN") or not os.environ.get("DATABASE_URL"):
    print("Please specify TOKEN and DATABASE_URL environment variables before starting the bot.")
    exit()

from telegram.ext import Filters

BOT_TOKEN = os.environ.get("7760196426:AAH3REc7UtXj_YiA0VuJpV2GwCorg9dvsCg")
DB_URI = os.environ.get("mongodb+srv://krishnaonly999:Krishdiya07@cluster0.h4rzpxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUDO_USERS = [
    1412086585
]
SUDO = Filters.user(SUDO_USERS)
LOG_CHAT = -1001336747262
