import functions as cmf
from client.client import m1kp
from client.client import events as evs

# Команды
cmds = {
    ".изменить": cmf.edit_msg_command,
    ".-": cmf.delete_msg_command,
    
    ".цитата": cmf.quote_command,
    ".диз": cmf.dislike_command,
    ".лайк": cmf.like_command,
    
    ".сейвы": cmf.view_saves_command,
    ".ос": cmf.clear_saves_command,
    ".ус": cmf.delete_save_command,
    ".сейв": cmf.save_command,
    
    ".тихийспам": cmf.silent_spam_command,
    ".спам": cmf.spam_command,
    
    ".процент": cmf.random_percent_command,
    ".данет": cmf.random_yes_or_no_command,
    ".шанс": cmf.random_chance_command,
    ".число": cmf.random_int_command,
    ".символ": cmf.random_char_command,
    
    ".хеш": cmf.random_hash_command,
    ".шифр": cmf.random_cezar_code_command,
    ".расшифр": cmf.cezar_decode_command,
    
    ".перевод": cmf.google_translate_command,
    ".время": cmf.time_now_command,
    
    ".автофарм": cmf.iris_autofarm_command,
    ".логгер": ...,
    ".лслоггер": ...,
    
    ".ботинфо": cmf.send_bot_info_command
}

# Функция запуска функций (команд)
async def run_function(func, msg):
    await func(msg)

# Реакция на команды
@m1kp.on(evs.NewMessage(outgoing=True))
async def command_function(event):
    text = event.text.split(" ")
    try:
        await run_function(cmds[text[0]], event)
    except:
        pass