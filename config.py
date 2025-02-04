from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")

ss = os.environ.get("TERMUX")
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = os.environ.get("YoMidobot")
# token = os.environ.get("7179039513:AAHPuNBfCLgq4Yf4zgLLKrQAPFKR4hZvqJM")
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
