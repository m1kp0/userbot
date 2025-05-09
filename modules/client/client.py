from telethon import *
from .config import API_ID, API_HASH
import random

api_id = int(API_ID)
api_hash = str(API_HASH)
session_name = str("M1KP_SESSION_YOU_CAN_DELETE_THIS_FILE")

# Бот
m1kp = TelegramClient(
    session=session_name,
    api_id=api_id,
    api_hash=api_hash
)
