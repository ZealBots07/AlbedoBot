from pyrogram.sessions import StringSession
from pyrogram.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(input("28408158: "))
API_HASH = input("ddda6703b42211276b28252aca309a2d: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
