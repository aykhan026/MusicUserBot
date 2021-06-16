# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s

import os
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from datetime import datetime, timedelta
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

WHITE_COMMAND = Li.WHITE_COMMAND

@Client.on_message(demon_killer_sigki
                   & misa_misa
                   & filters.command("now", prefixes=WHITE_COMMAND)
                   )   
async def show_current_playing_time(_, ryui: Message):
    start_time = ded.start_time
    playlist = ded.playlist
    if not start_time:
        pwn = await ryui.reply_text("Sinxronzasiya olunur @RoBotlarimTg", True) 
        await pwn.edit_text("Serverlə əlaqə yaradılır...") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
        await pwn.delete()            
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/f52e92e80e10aa7fc294c.jpg",
            caption="👨🏻‍💻 @RoBotlarımTg"
        )
        await wait_before_rm((hawk,), Kill_Time)                 
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if ded.msg.get('now') is not None:
        await ded.msg['now'].delete()
    ded.msg['now'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await ryui.delete()
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               aykhan_s
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
