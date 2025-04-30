from telethon import *
from .config import API_ID, API_HASH
import random

api_id = int(API_ID)
api_hash = str(API_HASH)
randint = random.randint(-9999999999999999999999, 99999999999999999999999)
session_name = str("M1KP_SESSION_" + str(randint) +
                   "_YOU_CAN_DELETE_THIS_FILE")

# Бот
m1kp = TelegramClient(
    session=session_name,
    api_id=api_id,
    api_hash=api_hash
)
