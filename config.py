#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

import os

API_ID = os.getenv("API_ID", "21185801")
API_HASH = os.getenv("API_HASH", "4235ef431f138309cb9f56ae179a24ba")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7581945436:AAGSyHehNl1g_J065dnkWhMy2ydS_rgX7ks")
ADMIN = int(os.getenv("ADMIN", "6928050839"))

DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002427015498")) #Channel Id
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002412832033"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://6ijziglmyz:EdlupMESij8BXWh5@cluster0.lv5i1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002090913537") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

ENABLE_FLOOD_WAIT = bool(os.getenv("ENABLE_FLOOD_WAIT", False)) # Set "True" For Enable Floodwait
FLOOD_WAIT_TIME = int(os.getenv("FLOOD_WAIT_TIME", 300)) #5min
