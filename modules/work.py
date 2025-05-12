from .functions import *
from .client import events as evs
from .client import m1kp
from .parser import *

# Команды
priv_cmds = {
    ".изменить": edit_msg_command,
    ".-": delete_msg_command,

    ".цитата": quote_command,
    ".диз": dislike_command,
    ".лайк": like_command,

    ".сейвы": view_saves_command,
    ".ос": clear_saves_command,
    ".ус": delete_save_command,
    ".сейв": save_command,

    ".тихийспам": silent_spam_command,
    ".спам": spam_command,

    ".процент": random_percent_command,
    ".данет": random_yes_or_no_command,
    ".шанс": random_chance_command,
    ".число": random_int_command,
    ".символ": random_char_command,

    ".вебскрин": web_screen_command,
    ".анекдот": random_joke_command,
    ".фраза": random_phrase_command,

    ".хеш": random_hash_command,
    ".шифр": random_cezar_code_command,
    ".расшифр": cezar_decode_command,
    ".залго": break_text_command,

    # ".перевод": google_translate_command,
    ".время": time_now_command,

    ".автофарм": iris_autofarm_command,
}

global deepseek_en
global auto_dot
global symbol
deepseek_en = False
auto_dot = False
symbol = "."


async def run_function(func, msg):
    await func(msg)


@m1kp.on(evs.NewMessage(outgoing=True))
async def command_function(event):
    text = event.text.split(" ", maxsplit=1)
    try:
        await run_function(priv_cmds[text[0]], event)

    except:
        pass


@m1kp.on(evs.NewMessage(outgoing=True))
async def command_function(event):
    text = event.text.split(" ", maxsplit=1)
    try:
        if text[0] == ".автосимвол":
            global auto_dot
            global symbol
            auto_dot = not auto_dot
            await event.delete()
            symbol = text[1] if auto_dot else ""

        elif text[0] == ".дипсик":
            global deepseek_en
            deepseek_en = not deepseek_en
            await m1kp.send_message(event.chat_id, "Дипсик включен!" if deepseek_en == True else "Дипсик выключен!", reply_to=event.message.id)

        if auto_dot == True:
            await event.edit(f"{event.text}{symbol}")
    except:
        pass


@m1kp.on(evs.NewMessage())
async def command_function(event):
    text = event.text.split(" ", maxsplit=1)
    try:
        if text[0].lower() == "ии" and deepseek_en == True and len(text) > 1:
            msg = await m1kp.send_message(event.chat_id, "Думаю..", reply_to=event.message.id)
            text = await generate_text("запомни: ответь мне максимально грубо и с матами, " + str(text[1]))
            await msg.edit(text)

    except ValueError as err:
        event.edit("Ошибка с дипсиком: " + str(err))
