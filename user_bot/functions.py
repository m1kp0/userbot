import datetime, random, os
from asyncio import sleep
from telethon import *
from googletrans import Translator
import client.client as cl

# Переменные
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
        try:
            if msg.is_reply:
                await delete_msg(await msg.get_reply_message()) # это изменил
                await delete_msg(msg)
            else:
                await error(msg, "Нет сообщения для удаления!")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def like_command(msg):
    if msg.text == ".лайк":
        try: await edit_msg(msg, "👍", 0)
        except Exception as e: await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def dislike_command(msg):
    if msg.text == ".диз":
        try: await edit_msg(msg, "👎", 0)
        except Exception as e: await error(msg, f"Что-то пошло не так, ошибка: {e}")

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
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.смс (кол-во смс) (смс)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".сейв":
        try:
            if msg.is_reply:
                saved_msgs.append(await msg.get_reply_message().text)
                await edit_msg(msg, "Добавлено в сохранённые", 0)
            else:
                try:
                    saved_msgs.append(text[1])
                    await edit_msg(msg, f"Добавлено в сохранённые: {text[1]}", 0)
                except:
                    await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.сейв (текст/ответ)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def delete_save_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == (".удалить_сейв" or ".ус"):
        try:
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
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def clear_saves_command(msg):
    if msg.text == (".очистить_сейвы" or ".ос"):
        try:
            if saved_msgs: 
                saved_msgs.clear()
                await edit_msg(msg, "Удалены все сохранённые сообщения", 0)
            else: 
                await error(msg, "Нет сохранений")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

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
        try:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            await edit_msg(msg, f"Время сейчас: {time_now}", 0)
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

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
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.процент (текст/ответ)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")


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
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.шанс (текст/ответ)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

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
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.данет (текст/ответ)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def iris_autofarm_command(msg):
    text = msg.text.split(" ", maxsplit=1)
    if text[0] == ".автофарм":
        try:
            if text[1] == "вкл": enabled = True
            else: enabled = False
            if enabled: await edit_msg(msg, "Автофарм ириса включен", 0)
            else: await edit_msg(msg, "Автофарм ириса выключен", 0)
            while enabled:
                await send_msg(cl.m1kp, msg.chat_id, "Ферма")
                await sleep(14460)
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена с ошибками\n[.автофарм (вкл/выкл)]")
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")

async def google_translate_command(msg): # тут есть небольшой баг, бот пока что не может перевести ответы не на русский, а на другйо язык. надо задавать язык в самом ответе, либо копировать его
    text1 = msg.text.split(" ", maxsplit=1)
    if text1[0] == ".перевод":
        reply = await msg.get_reply_message()
        tr = Translator()
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
            await edit_msg(msg, "Перевожу", 0)
            tred_text = tr.translate(text_to_tr, dest=lang).text
            await edit_msg(msg, f"перевод {text_to_tr} на {lang}:\n{tred_text}", 0)
        except ValueError:
            await error(msg, "Ошибка: команда не заполнена или заполнена не правильно\n[.перевод (текст/ответ) -(язык)]", 0)
        except Exception as e:
            await error(msg, f"Что-то пошло не так, ошибка: {e}")
