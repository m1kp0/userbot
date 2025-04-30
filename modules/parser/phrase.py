from bs4 import BeautifulSoup
import requests
import random

urls = [
    "https://www.anekdot.ru/last/aphorism/",
    "https://www.anekdot.ru/release/aphorism/week/",
    "https://www.anekdot.ru/release/aphorism/month/",
    "https://www.anekdot.ru/release/aphorism/year/",
    "https://www.anekdot.ru/random/aphorism/"
]


def parse_phrase():
    req = requests.get(urls[random.randint(0, 4)])
    soup = BeautifulSoup(req.text, "html.parser")
    jokes = soup.find_all("div", class_="text")
    return [i.text for i in jokes]
