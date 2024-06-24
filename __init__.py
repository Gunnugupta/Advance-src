#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("API_ID", default=21551881, cast=int)
API_HASH = config("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")
BOT_TOKEN = config("BOT_TOKEN", "7335340628:AAGfL-bshLeGzIDIG3frrTr8Tkmx1nOACeU")
SESSION = config("SESSION", "BQFI2wkABIamBBevaz0sU3BYWPzqOmmzsLOSs3iXjNMAX95WvcnRfFE3GID1MtaYVMpRdR30KWJ_dXLKv6ZpXn2goi8guNiXRj6Ikl0bdpXDgREvMWOvWFrSs49mAtfTRCyjipDHLRnKhygw-eAnPDX4uKESLQIBKZR5nPqY-alkvJqb3ahSPS2bPZ36woQi6VrFZimCFmuaoHxTEStq6fUpEmIr7oaRCSBTZyw_RmFVv8HUwWwHPchX_9GaOx4o7TFaaIlmmxMnHXLiyEiv3f5ZPM6lDJoUdbxq3F-Bjwwbo8ZpBEMqHyEn9GPY0TXLjPlnvVgiKlPtAKGu1XY0D-uVu8_TagAAAAGpbdleAA")
FORCESUB = config("FORCESUB", "moviesworldupdates")
AUTH = config("AUTH", "6359874284")
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
