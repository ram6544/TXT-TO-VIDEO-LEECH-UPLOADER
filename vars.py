

from os import environ

API_ID = int(environ.get("API_ID", "28389286"))
API_HASH = environ.get("API_HASH", "b88da5f4f338cca30f8ea5fb53cb083b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8382290189:AAFN8TDWswjEq1ccvAyvHcpHhOevaCZ_bik")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/+5H5tJB8hlJo2MjU1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6334323103").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "6334323103"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://divyanshshukla5375_db_user:1kZ2dsVTktdMljpr@cluster0.lo5qk5v.mongodb.net/?appName=Cluster0")









