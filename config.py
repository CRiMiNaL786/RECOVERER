import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}
SUDOERS = list(map(int, getenv("SUDOERS", "").split()))
API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
DB_URL = getenv("DATABASE_URL", "")
