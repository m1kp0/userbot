from .client import *


def start_bot():
    print("Бот запущен!")
    m1kp.start()
    m1kp.run_until_disconnected()
