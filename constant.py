import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()

# guildIds = [833210288681517126] # test discord server
guildIds = None # force global commands

BACKUP_DIR = os.getenv("BACKUP_DIR")
TOKEN = os.getenv("TOKEN")
