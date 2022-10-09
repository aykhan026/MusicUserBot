
# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMK

import os
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

DYNO_COMMAND = Li.DYNO_COMMAND

@Client.on_message(demon_killer_sigki
                   & senzo_kryo_ni
                   & misa_misa
                   & filters.command("skip", prefixes=DYNO_COMMAND)
                   ) 
async def skip_track(_, ryui: Message):
    playlist = ded.playlist
    if len(ryui.command) == 1:
        await ded.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(ryui.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} {i}")
            hawk = await ryui.reply_text("\n".join(text))
            await ded.send_playlist()
        except (ValueError, TypeError):
            pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
            await pwn.edit_text("Serverlə əlaqə yaradılır...") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
            await pwn.delete() 
            hawk = await ryui.reply_text(
                f"**Musiqini dəyişdirdim**",    
                                disable_web_page_preview=True
                                )
        await wait_before_rm((hawk, ryui), Kill_Time)
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               ☠BOT_RAMO☠
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 