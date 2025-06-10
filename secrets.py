import os

from telegram.ext import Filters

# Direct configuration
BOT_TOKEN = "7760196426:AAH3REc7UtXj_YiA0VuJpV2GwCorg9dvsCg"
DB_URI = "mongodb+srv://krishnaonly999:Krishdiya07@cluster0.h4rzpxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Sudo users (IDs as integers)
SUDO_USERS = [7171541681, 6685624393]  # Replace with actual Telegram user IDs

# Filters for sudo users
SUDO = Filters.user(user_id=SUDO_USERS)

# Logging group/channel chat ID
LOG_CHAT = -1002153866511