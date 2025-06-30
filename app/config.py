from os import environ, chdir
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv("../.env")
PYTHONPATH = environ.get("PYTHONPATH")
chdir(PYTHONPATH)


@dataclass
class Config:
    VERSION = environ.get("VERSION")
    BOT_TOKEN = environ.get("BOT_TOKEN")
    TELEGRAM_LINK = environ.get("TELEGRAM_LINK")
    MAIL_LINK = environ.get("MAIL_LINK")
    WHATSAPP_LINK = environ.get("WHATSAPP_LINK")
    VK_LINK = environ.get("VK_LINK")
    ADMIN_IDS = environ.get("ADMIN_IDS").split(", ")
