import datetime
import requests
import random
from g4f.client import Client
from asyncio import sleep
from telethon import *
from googletrans import Translator
from .client import client as cl

# Переменные
generator = Client()
tr = Translator()
saved_msgs = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890,./;[}{]*-+<>!@#$%^&*()_№:?=|"


async def edit_msg(msg, text):
    await msg.edit(text)


async def send_msg(bot, chat_id, text):
    await bot.send_message(chat_id, text)


async def delete_msg(msg):
    await msg.delete()


async def error(msg, text):
    await edit_msg(msg, text)
    await sleep(2)
    await delete_msg(msg)


async def get_reply(msg):
    replied_message = await msg.get_reply_message()
    return replied_message


async def delete_msg_command(msg):
    reply = await get_reply(msg)
    if msg.is_reply:
        await delete_msg(reply)
        await delete_msg(msg)
    else:
        await error(msg, "Нет сообщения для удаления!")


async def like_command(msg):
    await edit_msg(msg, "👍")


async def dislike_command(msg):
    await edit_msg(msg, "👎")


async def spam_command(msg):
    reply = await get_reply(msg)
    text = msg.text.split(" ", maxsplit=2)
    try:
        text_to_sms = reply.text if msg.is_reply else text[2]

        await edit_msg(msg, "Сообщения отправляются..")
        for i in range(int(text[1])):
            await send_msg(cl.m1kp, msg.chat_id, text_to_sms)
            await sleep(0.1)

        await delete_msg(msg)
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.спам (кол-во смс) (текст)]")


async def save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if msg.is_reply:
        reply = await get_reply(msg)
        saved_msgs.append(reply.text)
        await edit_msg(msg, "Добавлено в сохранённые")
    else:
        try:
            saved_msgs.append(text[1])
            await edit_msg(msg, f"Добавлено в сохранённые: {text[1]}")
        except:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.сейв (текст/ответ)]")


async def delete_save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    if msg.is_reply:
        if saved_msgs and (reply.text in saved_msgs):
            saved_msgs.remove(reply.text)
            await edit_msg(msg, "Удалено из сохранённых")
        else:
            await edit_msg(msg, f"Не найдено в сохранённых")
    else:
        try:
            if saved_msgs and text[1] in saved_msgs:
                saved_msgs.remove(text[1])
                await edit_msg(msg, f"Удалено из сохранённых: {text[1]}")
            else:
                await edit_msg(msg, f"Не найдено в сохранённых: {text[1]}")
        except:
            error(
                msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.удалить_сейв (текст/ответ)]")


async def clear_saves_command(msg):
    if saved_msgs:
        saved_msgs.clear()
        await edit_msg(msg, "Удалены все сохранённые сообщения")
    else:
        await error(msg, "Нет сохранений")


async def view_saves_command(msg):
    if saved_msgs:
        await edit_msg(msg, "Сохранённые сообщения:")
        for i in saved_msgs:
            await send_msg(cl.m1kp, msg.chat_id, i)
    else:
        await error(msg, "Нет сохранений")


async def time_now_command(msg):
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    await edit_msg(msg, f"Время сейчас: {time_now}")


async def random_percent_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    await edit_msg(msg, "Думаю..")
    await sleep(random.randint(1, 3))
    try:
        text_to_percent = reply.text if msg.is_reply else text[1]
        await edit_msg(msg, f"Думаю, {text_to_percent} на {random.randint(0, 100)}%")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.процент (текст/ответ)]")


async def random_chance_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    chance = random.randint(0, 100)
    reply = await get_reply(msg)
    await edit_msg(msg, "Думаю..")
    await sleep(random.randint(1, 3))
    try:
        text_to_chance = reply.text if msg.is_reply else text[1]
        await edit_msg(msg, f"Шанс того, что {text_to_chance} - {chance}%")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.шанс (текст/ответ)]")


async def random_yes_or_no_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    yes_or_no = random.randint(1, 2)
    reply = await get_reply(msg)
    await edit_msg(msg, "Думаю..")
    await sleep(random.randint(1, 3))
    try:
        text_to_yes_or_no = reply.text if msg.is_reply else text[1]
        choise_yes_or_no = "Да" if yes_or_no == 1 else "Нет"
        choise_yes_or_no_2 = "" if yes_or_no == 1 else "не"
        await edit_msg(msg, f"{choise_yes_or_no}, {choise_yes_or_no_2} {text_to_yes_or_no}")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.данет (текст/ответ)]")


async def random_int_command(msg):
    text = msg.text.split(" ", maxsplit=2)
    try:
        randint = random.randint(int(text[1]), int(text[2]))
        await edit_msg(msg, f"Рандомное число от {text[1]} до {text[2]} - {randint}")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.число (число1, число2)]")


async def random_char_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        text_to_random_char = reply.text if msg.is_reply else text[1]
        randchar = random.choice(text_to_random_char)
        await edit_msg(msg, f"Рандомный символ в {text_to_random_char} - {randchar}")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.символ (текст/ответ))]")


async def random_hash_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        text_to_random_hash = reply.text if msg.is_reply else text[1]
        randhash = hash(text_to_random_hash)
        await edit_msg(msg, f"{randhash}")
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.хеш (текст/ответ))]")


async def random_cezar_code_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        text_to_random_cezar_code = reply.text if msg.is_reply else text[1]
        randcode = ""

        for i in text_to_random_cezar_code:
            pos = alphabet.find(i)
            new_pos = pos + 1
            randcode += alphabet[new_pos] if i in alphabet else i

        await edit_msg(msg, randcode)
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.шифр (текст/ответ))]")


async def cezar_decode_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        text_to_decode = reply.text if msg.is_reply else text[1]
        randcode = ""

        for i in text_to_decode:
            pos = alphabet.find(i)
            old_pos = pos - 1
            randcode += alphabet[old_pos] if i in alphabet else i

        await edit_msg(msg, randcode)
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.расшифр (текст/ответ))]")


async def iris_autofarm_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    try:
        enabled = True if text[1] == "вкл" else False
        await edit_msg(msg, "Автофарм ириса включен: фарм раз в 10 часов") if enabled else await edit_msg(msg, "Автофарм ириса выключен")
        while enabled:
            await send_msg(cl.m1kp, msg.chat_id, "Ферма\nУрожайность +999")
            await sleep(36000)  # 10 Часов
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.автофарм (вкл/выкл)]")


# тут есть небольшой баг, бот пока что не может перевести ответы на другой язык.
async def google_translate_command(msg):
    reply = await get_reply(msg)
    try:
        if msg.is_reply:
            text_to_tr = reply.text
        else:
            _, *text = msg.raw_text.split(" ")
            text_to_tr = " ".join(text).strip()

        if "-" in text_to_tr:
            text_parts = text_to_tr.split("-")
            text_to_tr = text_parts[0].strip()
            lang = text_parts[1].strip()
        else:
            lang = 'ru'

        await edit_msg(msg, "Перевожу..")
        tred_text = tr.translate(text_to_tr, dest=lang).text
        await edit_msg(msg, f"перевод {text_to_tr} на {lang}:\n{tred_text}")
    except ValueError:
        await error(msg, "Ошибка: команда не заполнена или заполнена не правильно\n[.перевод (текст/ответ) -(язык)]")
    except Exception as e:
        await error(msg, f"Что-то пошло не так, попробуйте еще раз")


async def silent_spam_command(msg):
    text = msg.text.split(" ", maxsplit=2)
    reply = await get_reply(msg)
    try:
        text_to_sms = reply.text if msg.is_reply else text[2]
        await edit_msg(msg, "Сообщения отправляются..")
        for i in range(int(text[1])):
            # Не работает через функцию send_msg
            silent_msg = await cl.m1kp.send_message(msg.chat_id, text_to_sms)
            await sleep(0.4)
            await delete_msg(silent_msg)

        await delete_msg(msg)
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.тихийспам (кол-во смс) (текст)]")


async def edit_msg_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        if msg.is_reply:
            await edit_msg(reply, text[1])
            await delete_msg(msg)
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.изменить (текст)]")


async def quote_command(msg):
    reply = await get_reply(msg)
    quote_bot = "@QuotLyBot"
    quote_chat = await reply.forward_to(quote_bot) if msg.is_reply else await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.цитата (ответ)]")
    await edit_msg(msg, "Создаю цитату..")
    async with cl.m1kp.conversation(quote_bot) as conv:
        res = await conv.get_response(quote_chat.id)
        await cl.m1kp.send_read_acknowledge(conv.chat_id)
        await delete_msg(msg)
        await send_msg(cl.m1kp, msg.chat_id, res)


async def generate_img_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    reply = await get_reply(msg)
    try:
        prompt_def_lang = reply if msg.is_reply else text[1]
        await edit_msg(msg, f"Генерирую {prompt_def_lang}..")
        prompt_en = tr.translate(prompt_def_lang, dest="en").text
        await edit_msg(msg, f"Генерирую {prompt_def_lang} ({prompt_en})..")
        res = await generator.images.generate(
            model="flux",
            prompt=prompt_def_lang,
            response_format="url"
        )
        url = res.data[0].url
        data = requests.get(url).content
        with open("generated_img.jpg", "wb") as file:
            img = file.write(data)
            await cl.m1kp.send_file(msg.chat_id, img, caption=f'Сгенерировал картинку по запросу: {prompt_def_lang}\nURL: {url}')
    except:
        await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.ген (текст)]")


async def send_bot_info_command():
    ...
