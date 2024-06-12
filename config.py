from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26545740")
    API_HASH = environ.get("API_HASH", "108df940118cde6c5f524f4d439a19d3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7403427888:AAFGmYRVhHMnhoBL8fvqOFyb7PIhmvfOXZc") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
