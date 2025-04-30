from .functions import *
from .client import events as evs
from .client import m1kp

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
    ".анекдот": random_joke_command,
    ".фраза": random_phrase_command,

    ".хеш": random_hash_command,
    ".шифр": random_cezar_code_command,
    ".расшифр": cezar_decode_command,

    ".перевод": google_translate_command,
    ".время": time_now_command,

    ".автофарм": iris_autofarm_command,
    # ".ген": generate_img_command
}


async def run_function(func, msg):
    await func(msg)


@m1kp.on(evs.NewMessage(outgoing=True))
async def command_function(event):
    text = event.text.split(" ")
    try:
        await run_function(priv_cmds[text[0]], event)
    except:
        pass
