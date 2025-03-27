from telethon import *
from client.config import API_ID, API_HASH
import random

# Конфигурация
api_id = int(API_ID)
api_hash = str(API_HASH)
randint = random.randint(-999999999999999, 999999999999999)
session_name = str(hash(random.randint(randint, randint)))

# Бот
m1kp = TelegramClient(
    session=session_name,
    api_id=api_id, 
    api_hash=api_hash
)