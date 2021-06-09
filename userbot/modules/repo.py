
import asyncio
from collections import deque

from telethon.tl.functions.users import GetFullUserRequest

from userbot import *
from PETERCORDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=f"repo$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    await edit_or_reply(event, "REPO PETERCORD\n\n**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [𝗣 𝗘 𝗧 𝗘 𝗥 𝗖 𝗢 𝗥 𝗗](https://github.com/IlhamMansiez/PETERCORDBOT)\n\n [𝗢 𝗪 𝗡 𝗘 𝗥 𝗦](t.me/diemmmmmmmmmm)\n\n [GRUP SUPPORT](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**")
    animation_chars = [
        "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [𝗣 𝗘 𝗧 𝗘 𝗥 𝗖 𝗢 𝗥 𝗗](https://github.com/IlhamMansiez/PETERCORDBOT)\n\n [𝗢 𝗪 𝗡 𝗘 𝗥 𝗦](t.me/diemmmmmmmmmm)\n\n [GRUP SUPPORT](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
