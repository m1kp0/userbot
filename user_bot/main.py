
'''
_______________________________________________________________________________________________

до сих пор есть баги и ошибки, потихоньку всё исправляю. Бота использовать не рекомендую.
_______________________________________________________________________________________________

обнова:
[v] - версия
[+] - добавлено
[/] - пофикшено
_______________________________________________________________________________________________

[v] - 0.5
[+] название бота (m1kp)
[+] цветная командная строка
[+] визуальная имба запуск в командной строке
[+] возможность использовать некоторые команды с ответами на другие сообщения
[+] переводчик
[+] уведомления об ошибках в командах
[+] рандомное название сессии
[/] баг с буквами вместо точки 
[/] баг с командами типа .сейвы бот читал как .сейв и выдавал ошибку, хз как объяснить
________________________________________________________________________________________________
'''

# импорт
from telethon import *
from googletrans import Translator
from colorama import Fore, init
import datetime, time, random, os, configparser

# инит для командной строки
init()

# функции старта
conf = configparser.ConfigParser()
configfile_is_on_pc = False
print(Fore.MAGENTA)
print("███╗░░░███╗░░███╗░░██╗░░██╗██████╗░")
print("████╗░████║░████║░░██║░██╔╝██╔══██╗")
print("██╔████╔██║██╔██║░░█████═╝░██████╔╝")
print("██║╚██╔╝██║╚═╝██║░░██╔═██╗░██╔═══╝░")
print("██║░╚═╝░██║███████╗██║░╚██╗██║░░░░░")
print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░")
print("\n\n[Действия]:\n1. [Запуск бота]\n2. [Посмотреть команды бота]\n3. [Обновить бота] (не работает, пока что)\n4. [Остановить бота]\n5. [Очистить]\n6. [Закрыть программу]")

def select_deystvie():
    print(Fore.MAGENTA)
    cmd = input("[Выберите действие]: ")
    if cmd == ("1" or "Запуск бота" or "запуск бота"):
        print(Fore.WHITE)
        print(Fore.RED + "Примечание: не спамьте много, это нагружает сервера телеграма и вас могут забанить.\nРазработчик (я) не несу ответственности за ваши действия, если вас забанят - ваши проблемы.\n")
        print(Fore.GREEN + "Запуск..")
        print(Fore.GREEN + "! Не бойтесь вводить свои данные (это нужно не мне, а библиотеке бота). Я не смогу войти в ваш аккаунт.")
        print(Fore.WHITE)

        # начало работы
        def find_cfg_file():
            name = "m1kp_userbot_config.ini"
            for root, dirs, files in os.walk("C:"):
                if "m1kp_userbot_config.ini" in files:
                    print("файл есть!")

            return True
        
        if find_cfg_file():
            conf.read("m1kp_userbot_config.ini")

            # переменные
            zametks = []
            api_id = int(conf["SETTINGS"]["API_ID"]) # 25542343
            api_hash = str(conf["SETTINGS"]["API_HASH"]) # "7a1eaa42fbce44a3afcf8b20449653d4"
            randint = random.randint(-999999999999999, 999999999999999)
            session_name = str(hash(random.randint(randint, randint)))

            # бот
            m1kp = TelegramClient(
                session=session_name,
                api_id=api_id, 
                api_hash=api_hash
            )

            # функции
            # удаление сообщения
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.-"))
            async def delete_msg(event):
                reply = await event.get_reply_message()
                
                if event.text == ".-":
                    if event.is_reply:
                        await reply.delete()
                        await event.delete()
                    else:
                        await event.edit("нет сообщения для удаления!")
                        time.sleep(2)
                        await event.delete()

            # пр
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.пр"))
            async def pr(event):
                _, *text = event.raw_text.split(" ")
                if text[0] == ".пр":
                    text_to_select = " ".join(text).strip()

                    if "-" in text:
                        text_parts = text_to_select.split("-")
                        text_to_select = text_parts[0].strip()
                        select = text_parts[1].strip()

                    try:
                        if select == "1":
                            await event.edit("П")
                            time.sleep(0.1)
                            await event.edit("Пр")
                            time.sleep(0.1)
                            await event.edit("При")
                            time.sleep(0.1)
                            await event.edit("Прив")
                            time.sleep(0.1)
                            await event.edit("Приве")
                            time.sleep(0.1)
                            await event.edit("Привет")
                            time.sleep(0.1)
                            await event.edit("Привет!")
                        elif select == "2":
                            for i in range(1, 100):
                                time.sleep(0.1)
                                await event.edit("р----------------")
                                time.sleep(0.1)
                                await event.edit("-пр-------------")
                                time.sleep(0.1)
                                await event.edit("--пр------------")
                                time.sleep(0.1)
                                await event.edit("---пр-----------")
                                time.sleep(0.1)
                                await event.edit("----пр----------")
                                time.sleep(0.1)
                                await event.edit("-----пр---------")
                                time.sleep(0.1)
                                await event.edit("------пр--------")
                                time.sleep(0.1)
                                await event.edit("-------пр-------")
                                time.sleep(0.1)
                                await event.edit("--------пр------")
                                time.sleep(0.1)
                                await event.edit("---------пр-----")
                                time.sleep(0.1)
                                await event.edit("----------пр----")
                                time.sleep(0.1)
                                await event.edit("-----------пр---")
                                time.sleep(0.1)
                                await event.edit("------------пр--")
                                time.sleep(0.1)
                                await event.edit("-------------пр-")
                                time.sleep(0.1)
                                await event.edit("--------------пр")
                                time.sleep(0.1)
                                await event.edit("----------------п")
                        elif select == "3":
                            await event.edit("Ч")
                            await event.edit("ЧУ")
                            await event.edit("ЧУВ")
                            await event.edit("ЧУВА")
                            await event.edit("ЧУВАА")
                            await event.edit("ЧУВААА")
                            await event.edit("ЧУВАААА")
                            await event.edit("ЧУВААААА")
                            await event.edit("ЧУВАААААА")
                            await event.edit("ЧУВАААААААК З")
                            await event.edit("ЧУВАААААААК ЗД")
                            await event.edit("ЧУВАААААААК ЗДА")
                            await event.edit("ЧУВАААААААК ЗДАР")
                            await event.edit("ЧУВАААААААК ЗДАРО")
                            await event.edit("ЧУВАААААААК ЗДАРОВ")
                            await event.edit("ЧУВАААААААК ЗДАРОВА")
                    except:
                        await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.пр -(выбор)]")
                        time.sleep(2)
                        await event.delete()

            # подожди
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.жди"))
            async def sec_wait(event):
                if event.text == ".жди":
                    await event.edit("подожди 5 сек пж")
                    time.sleep(3)
                    await event.edit("я чуть занят просто")

            # лайк
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.лайк"))
            async def like(event):
                if event.text == ".лайк":
                    await event.edit("👍")

            # диз
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.диз"))
            async def dislike(event):
                if event.text == ".диз":
                    await event.edit("👎")

            # скрипты
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.скрипт"))
            async def script(event):
                _, *text = event.raw_text.split(" ")
                if text[0] == ".домен":
                    text_to_select = " ".join(text).strip()

                    if "-" in text_to_select:
                        text_parts = text_to_select.split("-")
                        select = text_parts[1].strip()

                    try:
                        if select == "лб":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/DMO/refs/heads/main/ladder_breaker.lua'))()") # ладдер бреакер дмо
                        elif select == "лбв6":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/DMO/refs/heads/main/ladder_breaker_v6_beta.lua'))()") # ладдер бреакер 6
                        elif select == "чатбайпасс":
                            await event.edit("loadstring(game:HttpGet'https://raw.githubusercontent.com/m1kp0/universal_scripts/refs/heads/main/chat_bypass.lua')()") # чат байпасс
                        elif select == "иур":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/alajayid/infiniteyield-reborn-reborn/master/source'))()") # инфините уиелд реборн
                        elif select == "патх": 
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/universal_scripts/refs/heads/main/ONLY-PC_pathing'))()") # pathing
                        elif select == "лбб":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/lucky_block_battleground/refs/heads/main/lbb.lua'))()") # лаки блоки
                        elif select == "беар":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/auto_farm/refs/heads/main/bear_alpha.lua'))()") # беар альфа автофарм
                        elif select == "фриадмин":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/free_admin/refs/heads/main/free_admin_script.lua'))()") # фри админ скрипт
                        elif select == "тох":
                            await event.edit("loadstring(game:HttpGet('https://raw.githubusercontent.com/m1kp0/tower_of_hell/refs/heads/main/toh.lua'))()") # тавер оф хелл
                        else:
                            await event.edit("у меня нет такого скрипта")
                            time.sleep(2)
                            await event.delete()
                    except:
                        await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.скрипт -(название)]")
                        time.sleep(3)
                        await event.delete()

            # домен
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.домен"))
            async def domen(event):
                text = event.text.split(" ")
                if text[0] == ".домен": 
                    _, *text = event.raw_text.split(" ")
                    text_to_select = " ".join(text).strip()

                    if "-" in text_to_select:
                        text_parts = text_to_select.split("-")
                        select = text_parts[1].strip()

                    try:
                        if select == "дельта":
                            await event.edit("deltaexploits.gg")
                        elif select == "кодекс":
                            await event.edit("codex.lol")
                        elif select == "крнл":
                            await event.edit("krnl.cat")
                        elif select == "хено":
                            await event.edit("xeno.now")
                        else:
                            await event.edit("у меня нет этого домена")
                    except:
                        await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.домен -(название)]")
                        time.sleep(3)
                        await event.delete()

            # спам
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.смс"))
            async def spam(event):
                texta = event.text.split(" ")
                if texta[0] == ".смс":
                    reply = await event.get_reply_message()

                    try:
                        _, *text = event.raw_text.split(" ")
                        text_to_count = " ".join(text).strip()

                        if "-" in text_to_count:
                            text_parts = text_to_count.split("-")
                            text_to_count = text_parts[0].strip()
                            sms_count = text_parts[1].strip()

                        if event.is_reply:
                            await event.edit("смс отправляются")
                            for i in range(int(sms_count)):
                                await m1kp.send_message(event.chat_id, reply.text)
                                time.sleep(0.1)
                            
                            await event.delete()
                        else:
                            await event.edit("смс отправляются")
                            for i in range(int(sms_count)):
                                await m1kp.send_message(event.chat_id, texta[1])
                                time.sleep(0.1)
                            
                            await event.delete()
                    except:
                        await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.смс -(смс/ответ) (кол-во смс)]")
                        time.sleep(2)
                        await event.delete()


            # заметки функции
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"^\.сейв"))
            async def zametka_save(event):
                text = event.text.split(sep=None, maxsplit=1)
                if text[0] == ".сейв":
                    reply = await event.get_reply_message()

                    if event.is_reply:
                        zametks.append(reply.text)
                        await event.edit("добавлено в сохранённые")
                    else:
                        try:
                            zametks.append(text[1])
                            await event.edit(f"добавлено в сохранённые: {text[1]}")
                        except:
                            await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.сейв (текст/ответ)]")
                            time.sleep(2)
                            await event.delete()

            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.удалить_сейв"))
            async def zametka_delete(event):
                text = event.text.split(sep=None, maxsplit=1)
                if text[0] == ".удалить_сейв":
                    reply = await event.get_reply_message()

                    if event.is_reply:
                        if zametks and reply.text in zametks:
                            zametks.remove(reply.text)
                            await event.edit("удалено из сохранённых")
                        else:
                            await event.edit(f"не найдено в сохранённых")
                    else:
                        try:
                            if zametks and text[1] in zametks:
                                zametks.remove(text[1])
                                await event.edit(f"удалено из сохранённых: {text[1]}")
                            else:
                                await event.edit(f"не найдено в сохранённых: {text[1]}")
                        except:
                            await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.удалить_сейв (текст/ответ)]")
                            time.sleep(2)
                            await event.delete()

            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.очистить_сейвы"))
            async def clear_zametks(event):
                if event.text == ".очистить_сейвы":
                    zametks.clear()

                    if zametks: await event.edit("удалены все сохранённые сообщения")
                    else: await event.edit("нет сохранений")

            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.сейвы"))
            async def see_zametks(event):
                if event.text == ".сейвы":
                    if zametks:
                        for i in zametks:
                            await m1kp.send_message(event.chat_id, i)
                            await event.edit("сохранённые сообщения:")
                    else:
                        await event.edit("нет сохранений")

            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.см"))
            async def forward_sebe(event):
                if event.text == ".см":
                    reply = await event.get_reply_message()

                    if event.is_reply:
                        await m1kp.forward_messages("me", reply)
                        await event.edit("сообщение переслано себе")
                    else:
                        await event.edit("сообщение не найдено")
                        time.sleep(2)
                        await event.delete()

            # время сейчас
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.время"))
            async def vremya(event):
                if event.text == ".время":
                    time_now = datetime.datetime.now().strftime("%H:%M:%S")

                    await event.edit(f"время сейчас: {time_now}")

            # процент
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.процент"))
            async def percent(event):
                text = event.text.split(sep=None, maxsplit=1)
                if text[0] == ".процент":
                    reply = await event.get_reply_message()

                    await event.edit("я думаю..")
                    time.sleep(random.randint(1, 3))
                    if event.is_reply: 
                        await event.edit(f"я думаю, {reply.text} на {random.randint(0, 100)}%")
                    else: 
                        try: 
                            await event.edit(f"я думаю, {text[1]} на {random.randint(0, 100)}%")
                        except: 
                            await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.процент (текст/ответ)]")
                            time.sleep(2)
                            await event.delete()

            # вероятность
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.вероятность"))
            async def veroyatnoost(event):
                text = event.text.split(sep=None, maxsplit=1)
                if text[0] == ".вероятность":
                    reply = await event.get_reply_message()
                    veroyatnost = random.randint(0, 100)

                    await event.edit("я думаю..")

                    time.sleep(random.randint(1, 3))

                    if event.is_reply: 
                        await event.edit(f"вероятность, что {reply.text} - {veroyatnost}%")
                    else: 
                        try:
                            await event.edit(f"вероятность, что {text[1]} - {veroyatnost}%")
                        except:
                            await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.вероятность (текст/ответ)]")
                            time.sleep(2)
                            await event.delete()

            # да нет
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.данет"))
            async def danet(event):
                text = event.text.split(sep=None, maxsplit=1)
                if text[0] == ".данет":
                    reply = await event.get_reply_message()

                    await event.edit("я думаю..")
                    time.sleep(random.randint(1, 4))
                    danet = random.randint(1, 2)
                    if danet == 1:
                        if event.is_reply:
                            await event.edit(f"да, {reply.text}")
                        else:
                            try:
                                await event.edit(f"да, {text[1]}")
                            except:
                                await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.данет (текст/ответ)]")
                                time.sleep(2)
                                await event.delete()
                    else:
                        if event.is_reply:
                            await event.edit(f"нет, {reply.text}")
                        else:
                            try:
                                await event.edit(f"нет, {text[1]}")
                            except:
                                await event.edit("ошибка: команда не заполнена или заполнена с ошибками\n[.данет (текст/ответ)]")
                                time.sleep(2)
                                await event.delete()

            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.перевод"))
            async def perevod(event):
                text = event.text.split(sep=None, maxsplit=2)
                if text[0] == ".перевод":
                    reply = await event.get_reply_message()
                    tr = Translator()

                    try:
                        if event.is_reply:
                            text_to_tr = reply.text
                        else:
                            _, *text = event.raw_text.split(" ")
                            text_to_tr = " ".join(text).strip()

                        if "-" in text_to_tr:
                            text_parts = text_to_tr.split("-")
                            text_to_tr = text_parts[0].strip()
                            lang = text_parts[1].strip()
                        else:
                            lang = 'ru'

                        await event.edit("перевожу")
                        tred_text = tr.translate(text_to_tr, dest=lang).text
                        await event.edit(f"перевод {text_to_tr} на {lang}:\n{tred_text}")
                    except ValueError:
                        await event.edit("ошибка: команда не заполнена или заполнена не правильно\n[.перевод (текст/ответ) -(язык)]")
                        time.sleep(2)
                        await event.delete()
                    except Exception as e:
                        await event.edit(f"чтото пошло не так, код ошибки: {e}")

            # команды
            @m1kp.on(events.NewMessage(outgoing=True, pattern=r"\.команды"))
            async def komandi(event):
                await event.edit("[.-] - удаление сообщения;\n[.пр] (1/2/3) - привет;\n[.жди] - просит собеседника подождать;\n[.лайк] - лайк;\n[.диз] - дизлайк;\n[.скрипт -(лб/лбв6/чатбайпасс/иур/патх/лбб/фриадмин/тох)] - даёт скрипт;\n[.домен -(дельта/кодекс/крнл/хено/еще добавлю)] - дает домен официального сайта эксплоита\n[.сейв (текст/ответ)] - сохраняет сообщение;\n[.удалить_сейв (текст/ответ)] - удалить сейв;\n[.очистить_сейвы] - очистить сейвы;\n[.сейвы] - показывает все сохранённые сообщения;\n[.время] - точное время сейчас;\n[.см] - переслать сообщение самому себе;\n[.процент (текст/ответ)] - рандомное число (0-100%);\n[.вероятность (текст/ответ)] - рандомное число (0-100%);\n[.данет (текст/ответ)] - рандом (да/нет)\n[.смс (смс) -(кол-во смс)] - отправить смс\n[.перевести (текст/ответ) -(язык) ] - переводчик\n[.команды] - все команды;\n\nответ значит ответ на сообщение человека/бота")
        else:
            print(Fore.MAGENTA)

            conf["SETTINGS"] = {}
            conf["SETTINGS"]["API_ID"] = str(input("Введите свой API ID: "))
            conf["SETTINGS"]["API_HASH"] = str(input("Введите свой API HASH: "))

            with open("m1kp_userbot_config.ini", "w+") as cfg_file:
                conf.write(cfg_file)
                print("файл создан!")
                
            m1kp.start()
            m1kp.run_until_disconnected()

    elif cmd == ("2" or "Посмотреть команды бота" or "посмотреть команды бота"):
        print(Fore.WHITE)
        print("\n[.-] - удаление сообщения;\n[.пр] (1/2/3) - привет;\n[.жди] - просит собеседника подождать;\n[.лайк] - лайк;\n[.диз] - дизлайк;\n[.скрипт -(лб/лбв6/чатбайпасс/иур/патх/лбб/фриадмин/тох)] - даёт скрипт;\n[.домен -(дельта/кодекс/крнл/хено/еще добавлю)] - дает домен официального сайта эксплоита\n[.сейв (текст/ответ)] - сохраняет сообщение;\n[.удалить_сейв (текст/ответ)] - удалить сейв;\n[.очистить_сейвы] - очистить сейвы;\n[.сейвы] - показывает все сохранённые сообщения;\n[.время] - точное время сейчас;\n[.см] - переслать сообщение самому себе;\n[.процент (текст/ответ)] - рандомное число (0-100%);\n[.вероятность (текст/ответ)] - рандомное число (0-100%);\n[.данет (текст/ответ)] - рандом (да/нет)\n[.смс (смс) -(кол-во смс)] - отправить смс\n[.перевести (текст/ответ) -(язык)] - переводчик\n[.команды] - все команды;")
        print(Fore.YELLOW + "\nПримечание: ответ - это ответ на сообщение человека/бота")
        print(Fore.WHITE)
        select_deystvie()
    elif cmd == ("3" or "Обновить бота" or "обновить бота"):
        print(Fore.WHITE)
        print("! Действие в разработке, скоро оно будет добавлено")
        print(Fore.WHITE)
        select_deystvie()
    elif cmd == ("4" or "Остановить бота" or "остановить бота"):
        print(Fore.WHITE)
        print("Остановка бота..")

        try:
            m1kp.disconnect()
            print("Бот остановлен")
        except:
            print("Бот не был запущен")

        print(Fore.WHITE)
        select_deystvie()
    elif cmd == ("5" or "Очистить" or "Очистить"):
        os.system("cls")
        select_deystvie()
    elif cmd == ("6" or "Закрыть программу" or "закрыть программу"):
        exit(0)
    else:
        print(Fore.YELLOW)
        print("Выбрано несуществующее действие: чтобы выбрать действие - поставьте цифру (номер действия), либо напишите название действия")
        print(Fore.WHITE)
        select_deystvie()  

select_deystvie()