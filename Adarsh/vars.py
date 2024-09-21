# # (c) adarsh-goel
# import os
# from os import getenv, environ
# from dotenv import load_dotenv



# load_dotenv()

# class Var(object):
#     MULTI_CLIENT = False
#     API_ID = int(getenv('API_ID'))
#     API_HASH = str(getenv('API_HASH'))
#     BOT_TOKEN = str(getenv('BOT_TOKEN'))
#     name = str(getenv('name', 'filetolinkbot'))
#     SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
#     WORKERS = int(getenv('WORKERS', '4'))
#     BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
#     PORT = int(getenv('PORT', 8080))
#     BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
#     PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
#     OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())  
#     NO_PORT = bool(getenv('NO_PORT', False))
#     APP_NAME = str(getenv('APP_NAME'))
#     OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
#     if 'DYNO' in environ:
#         ON_HEROKU = True
#         APP_NAME = str(getenv('APP_NAME'))
    
#     else:
#         ON_HEROKU = False
#     FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
#     HAS_SSL=bool(getenv('HAS_SSL',False))
#     if HAS_SSL:
#         URL = "https://{}/".format(FQDN)
#     else:
#         URL = "http://{}/".format(FQDN)
#     DATABASE_URL = str(getenv('DATABASE_URL'))
#     UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
#     BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 


# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', "18029060"))
    API_HASH = str(getenv('API_HASH', "c7e952440251e33bb5cce566b29f7254"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "7446514185:AAGF5vVhuGnQJc-t41RH_VpEqUO4rdFrdio"))
    name = str(getenv('name', 'THHREQBOT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '0'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1001992201683"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1277771711").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "Madara_Uchiaha"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://razibot:razibot@cluster0.daqud.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "The_Happy_Hours"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "0")).split())) 
