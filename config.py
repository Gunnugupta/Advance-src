from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21551881")
    API_HASH = environ.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7335340628:AAGfL-bshLeGzIDIG3frrTr8Tkmx1nOACeU") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7137515870').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
