from bs4 import BeautifulSoup
import requests
import random

urls = [
    "https://www.anekdot.ru/last/good/",
    "https://www.anekdot.ru/last/anekdot/",
    "https://www.anekdot.ru/random/anekdot/",
    "https://www.anekdot.ru/release/anekdot/week/",
    "https://www.anekdot.ru/release/anekdot/month/",
    "https://www.anekdot.ru/release/anekdot/year/",
    "https://www.anekdot.ru/tags/пошлые/5?type=anekdots",
    "https://www.anekdot.ru/release/anekdot/day/2025-03-31/",

    "https://anekdoty.ru/",
    "https://anekdoty.ru/korotkie/",
    "https://anekdoty.ru/pro-negrov/",
    "https://anekdoty.ru/pro-gitlera/",
    "https://anekdoty.ru/cherniy-yumor/",
    "https://anekdoty.ru/samye-smeshnye/",
    "https://anekdoty.ru/tupo-no-smeshno/",
    "https://anekdoty.ru/poshlye-anekdoty/10/",

    "https://anekdotov.net/intim/",
    "https://anekdotov.net/anekdot/",
    "https://anekdotov.net/anekdot/jew/",

    "https://www.maximonline.ru/entertainment/obyavleny-samye-smeshnye-anekdoty-2024-goda-id5823939/"
]


def parse_joke():
    req = requests.get(urls[random.randint(0, 19)])
    soup = BeautifulSoup(req.text, "html.parser")
    jokes = soup.find_all("div", class_="text") or soup.find_all(
        "div", class_="anekdot") or soup.find_all("div", class_="holder-body") or soup.find_all(
            "div", class_="ds-block-text text-style-body-1 ds-article-content__block ds-article-content__block_text")
    return [i.text for i in jokes]
