from os import environ 

class Config:
    API_ID = environ.get("API_ID", "14602734")
    API_HASH = environ.get("API_HASH", "b66b42bbe3af4110d4fffddc44d0280c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6480444276:AAGieHOq4rpDeFMYyTNpOF6jILE1iFr07uw") 
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
    
