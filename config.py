# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22642372"))
API_HASH = getenv("API_HASH", "cda9f2e2f1c28370447a79c3e39cbe88")
BOT_TOKEN = getenv("BOT_TOKEN", "7093354457:AAFndW4P05SpazTRtTr2xxlBOp-t_5WPxPA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6331847574").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://strong:strong@cluster0.ix7usa3.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1001835357010")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001835357010"))
