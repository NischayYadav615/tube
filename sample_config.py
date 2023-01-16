""" !/usr/bin/env python3
    -*- coding: utf-8 -*-
    Name     : inline-tube-mate [ Telegram ]
    Repo     : https://github.com/m4mallu/inine-tube-mate
    Author   : Renjith Mangal [ https://t.me/space4renjith ]
    Credits  : https://github.com/SpEcHiDe/AnyDLBot """

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5884076474:AAECzb9MHCp03LrvI8YKJ6YuX879gp7lBBY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19911978"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "e3f5848d4c384af9e6f1f52ca84c19c7")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "fase").split())

    # superusers to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "5826950002

").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority")

    # Force subscribe channel / group id starting with -100
    FORCE_SUB_CHAT = os.environ.get("FORCE_SUB_CHAT", "-1001881722859")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
