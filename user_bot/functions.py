import datetime, random, os
from asyncio import sleep
from telethon import *
import client.client as cl

# Сохраненные сообщения
saved_msgs = []

# "Глобальные" функции, используются в командах бота
async def edit_msg(msg, text, sleep_time):
    await msg.edit(text)
    await sleep(sleep_time)

async def send_msg(bot, chat_id, text):
    await bot.send_message(chat_id, text)

async def delete_msg(msg):
    await msg.delete()

async def error(msg, text):
    await edit_msg(msg, text, 0)
    await sleep(2)
    await delete_msg(msg)

# Команды
async def delete_msg_command(msg):    
    text = msg.text
    if text == ".-":
        if msg.is_reply:
            await delete_msg(await msg.get_reply_message()) # это изменил
            await delete_msg(msg)
        else:
            await error(msg, "Нет сообщения для удаления!")

async def like_command(msg):
    if msg.text == ".лайк":
        await edit_msg(msg, "👍", 0)

async def dislike_command(msg):
    if msg.text == ".диз":
        await edit_msg(msg, "👎", 0)

async def sms_command(msg):
    text = msg.text.split(" ", maxsplit=2)
    if text[0] == ".смс":
        try:
            if msg.is_reply:
                text_to_sms = await msg.get_reply_message().text
            else:
                text_to_sms = text[2]
            
            await edit_msg(msg, "Сообщения отправляются..", 0)
            for i in range(int(text[1])):
                await send_msg(cl.m1kp, msg.chat_id, text_to_sms)
                await sleep(0.1)
            
            await delete_msg(msg)
        except:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.смс (кол-во смс) (смс)]")

async def save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".сейв":
        if msg.is_reply:
            saved_msgs.append(await msg.get_reply_message().text)
            await edit_msg(msg, "Добавлено в сохранённые", 0)
        else:
            try:
                saved_msgs.append(text[1])
                await edit_msg(msg, f"Добавлено в сохранённые: {text[1]}", 0)
            except:
                await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.сейв (текст/ответ)]")

async def delete_save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == (".удалить_сейв" or ".ус"):
        if msg.is_reply:
            reply_text = msg.get_reply_message().text
            if saved_msgs and reply_text in saved_msgs:
                saved_msgs.remove(reply_text)
                await edit_msg(msg, "Удалено из сохранённых", 0)
            else:
                await edit_msg(msg, f"Не найдено в сохранённых", 0)
        else:
            try:
                if saved_msgs and text[1] in saved_msgs:
                    saved_msgs.remove(text[1])
                    await edit_msg(msg, f"Удалено из сохранённых: {text[1]}", 0)
                else:
                    await edit_msg(msg, f"Не найдено в сохранённых: {text[1]}", 0)
            except:
                error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.удалить_сейв (текст/ответ)]")

async def clear_saves_command(msg):
    if msg.text == (".очистить_сейвы" or ".ос"):
        if saved_msgs: 
            saved_msgs.clear()
            await edit_msg(msg, "Удалены все сохранённые сообщения", 0)
        else: 
            await error(msg, "Нет сохранений")

async def view_saves_command(msg):
    if msg.text == ".сейвы":
        if saved_msgs:
            await edit_msg(msg, "Сохранённые сообщения:", 0)
            for i in saved_msgs:
                await send_msg(cl.m1kp, msg.chat_id, i)
        else:
            await error(msg, "Нет сохранений")

async def time_now_command(msg):
    if msg.text == ".время":
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        await edit_msg(msg, f"Время сейчас: {time_now}", 0)

async def random_percent_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".процент":
        reply_text = await msg.get_reply_message()
        await edit_msg(msg, "Думаю..", 0)
        await sleep(random.randint(1, 3))
        try:
            if msg.is_reply: 
                await edit_msg(msg, f"Думаю, {reply_text} на {random.randint(0, 100)}%", 0)
            else: await edit_msg(msg, f"Думаю, {text[1]} на {random.randint(0, 100)}%", 0)
        except:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.процент (текст/ответ)]")


async def random_chance_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".шанс":
        reply_text = await msg.get_reply_message()
        chance = random.randint(0, 100)
        await edit_msg(msg, "Думаю..", 0)
        await sleep(random.randint(1, 3))
        try:
            if msg.is_reply: await edit_msg(msg, f"Шанс того, что {reply_text} - {chance}%", 0)
            else: await edit_msg(msg, f"Шанс того, что {text[1]} - {chance}%", 0)
        except:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.шанс (текст/ответ)]")

async def random_yes_or_no_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".данет":
        reply_text = await msg.get_reply_message().text
        yes_or_no = random.randint(1, 2)
        await edit_msg(msg, "Думаю..", 0)
        await sleep(random.randint(1, 3))
        try:
            if yes_or_no == 1:
                if msg.is_reply: await edit_msg(msg, f"Да, {reply_text}", 0)
                else: await edit_msg(msg, f"Да, {text[1]}", 0)
            else:
                if msg.is_reply: await edit_msg(msg, f"Нет, {reply_text}", 0)
                else: await edit_msg(msg, f"Нет, {text[1]}", 0)
        except:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.данет (текст/ответ)]")