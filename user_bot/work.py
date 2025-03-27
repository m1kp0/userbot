import functions as cmf
import run_bot as run
from client.client import m1kp
from client.client import events as evs

# Реакция на команды
@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.-"))
async def dmc(event): # delete message command
    await cmf.delete_msg_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.лайк"))
async def lc(event): # like command
    await cmf.like_command(event) 

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.диз"))
async def dc(event): # dislike command
    await cmf.dislike_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.смс"))
async def smsc(event): # sms command
    await cmf.sms_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.сейв"))
async def savec(event): # save command
    await cmf.save_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.удалить_сейв"))
async def dsc(event): # delete save command
    await cmf.delete_save_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.ус"))
async def sdsc(event): # short delete save command
    await cmf.delete_save_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.очистить_сейвы"))
async def csc(event): # clear saves command
    await cmf.clear_saves_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.ос"))
async def scsc(event): # short clear saves command
    await cmf.delete_save_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.сейвы"))
async def vsc(event): # view saves command
    await cmf.view_saves_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.время"))
async def tnc(event): # time now command
    await cmf.time_now_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.процент"))
async def rpc(event): # random percent command
    await cmf.random_percent_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.шанс"))
async def rcc(event): # random chance command
    await cmf.random_chance_command(event)
    
@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.данет"))
async def ryonc(event): # random yes or no command
    await cmf.random_yes_or_no_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.автофарм"))
async def iac(event): # iris autofarm command
    await cmf.iris_autofarm_command(event)

@m1kp.on(evs.NewMessage(outgoing=True, pattern=r"\.перевод"))
async def gtc(event): # google translate command
    await cmf.google_translate_command(event)
