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
API_ID = config("API_ID", default=26545740, cast=int)
API_HASH = config("API_HASH", "108df940118cde6c5f524f4d439a19d3")
BOT_TOKEN = config("BOT_TOKEN", "6997158337:AAFihbtMB2Jp3Agc6hmCojmw3W7a6vFIJz8")
SESSION = config("SESSION", "AQBvw20Ank_jstFhLe89xeA0qM4VM7X4uYtB_HQul6KLGu0dpn4WYN9HoIupz1bWBRYyrVY1JU9w93oWbyiUkLPX1yutPGl39gbx-VG2wiRUtsnmXUsfH6sI0BmXBIBle4ymu9-j37qyzN-0-cz4P4T9k_dWiJEf4Yjg4sxpFthQu-xFGqlE9i4P-MRs5DFmqkIxYWtu49iJiXKCUK1JUsbzEUj5cwfIn-NhLgw3EvlsCfaCbsK4Chq74PRoIvvJ07Jur-Ic4Hi8Tv7F3bgQK8cxgG3CKm535ZutE_SGbcLts6xUxWTSpOuxh-DLbrW0iFJqgJDu8FSlMQHlDw1yrENA6rglKwAAAAGgXFGNAA")
FORCESUB = config("FORCESUB", "testu7y")
AUTH = config("AUTH", "6820572640")
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
