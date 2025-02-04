from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = os.environ.get("24944143")
APP_HASH = os.environ.get("c3a7a7e23f79042411d74e870f480ae3")

ss = os.environ.get("1BJWap1sBu2NPLBbEj-URLUQYHZbi5C0p3u6uMEj86qMifIt0RpXr9iWWB2XvWB9t22TOFsfDPanTQ_8XEeI6ZUT2BdJ2UqMB7HEfRKMD6BDha44Bdf4H1xz_QtPbOGY4_cnQhH9odqvEWWm-XaDMDebaIMTguBae2txT9Vsf89qUeLAjpnxOFNvM9q6kZlNdDviZhDvh7rFI3JfprLp269uJLdOoq7mLzzP5U6B7E5opIpixHUcV13qIZxqNsEvc8c8N8SefBbFnG7bOxlG0WOFHm2bKh9rAuFTX1jvtnFp7PPecdfNbH1yXNpgUQ0pVknVU-Bi9eXiAI16_hNmQmuMITTRjxM4=")
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = os.environ.get("YoMidobot")
# token = os.environ.get("7179039513:AAHPuNBfCLgq4Yf4zgLLKrQAPFKR4hZvqJM")
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()