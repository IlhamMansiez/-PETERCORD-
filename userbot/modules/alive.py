#Ilham mansiez
#PetercordBot
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, PETERCORDversion
from PETERCORDBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# TENTANG AKU DAN DIA
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ππΈπ½ππΈπΉππ"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @diemmmmmmmmmm (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for @diemmmmmmmmmm

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

PETERCORD = bot.uid


edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
file2 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
file3 = "https://telegra.ph/file/e4142fc1d14bc3c8181a3.jpg"
file4 = "https://telegra.ph/file/2d2a335d26a0d33a1e385.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**β‘β‘π£ππ§ππ₯ππ’π₯π πππ ππ πππππβ‘β‘**__\n\n"

pm_caption += f"**ββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 β‘π£ππ‘πππ¨π‘πβ‘\n  **πΎ[{DEFAULTUSER}](tg://user?id={PETERCORD})πΎ**\n\n"
)
pm_caption += f"ββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `π§ππππ§ππ’π‘:` `2-2-7` \n"
pm_caption += f"β£β’β³β  `π©ππ₯π¦ππ’π‘:` `{PETERCORDversion}`\n"
pm_caption += f"β£β’β³β  `π¦π¨ππ’:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `ππππ‘π‘ππ:` [πΏπ΄ππ΄ππ²πΎππ³](https://t.me/TEAMSquadUserbotSupport)\n"
pm_caption += f"β£β’β³β  `ππ₯πππ§π’π₯:` [Ilham Mansiez](https://t.me/diemmmmmmmmmm)\n"
pm_caption += f"β£β’β³β  `π¦π¨π£π£π’π₯π§:` [PETERCORD](https://t.me/TEAMSquadUserbotSupport)\n"
pm_caption += f"ββββββββββββββββββ\n"
pm_caption += " [β‘REPOβ‘](https://github.com/IlhamMansiez/PETERCORDBOT) πΈ [πLicenseπ](https://github.com/IlhamMansiez/PETERCORDBOT/blob/master/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file1)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file2)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file3)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
