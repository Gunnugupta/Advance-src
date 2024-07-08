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
API_ID = config("API_ID", default=14602734, cast=int)
API_HASH = config("API_HASH", "b66b42bbe3af4110d4fffddc44d0280c")
BOT_TOKEN = config("BOT_TOKEN", "6480444276:AAGieHOq4rpDeFMYyTNpOF6jILE1iFr07uw")
SESSION = config("SESSION", "AQDe0e4Am7ZSmd0S3qcHtdXW8pLzd_BNfZijZ-YWlIfkMDLXYPLi5ChFXdWcJpDfehvugHcY05MDc3J9U7IlvkAq-56fgG5RlvP-SizVb5nmHrDZK8c7aE3CvaIR5sOaZS1Xlf7yrk0tEyFSbdfRZP6Lj6pDlE9Tph8d-vIDKZThgveeey8Iea_2bq-HgooHiBc1L2h9ntYRMNfg5W0xm6fSc7P_Xb_5LzSY3-erfO-wqOvkGhVA7lURfbGyBIaeHnzBMmkYmgH73kFAHyEJ-LjMS7ZJCVjYyZ6hJr6GbKraDI8Sk4-Ub3wu2LCq197jD5n7pHuYofzwn05U2FfcHqUhm12ubAAAAAG1G_KUAA")
FORCESUB = config("FORCESUB", "moviesworldupdates")
AUTH = config("AUTH", "7137515870")
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
