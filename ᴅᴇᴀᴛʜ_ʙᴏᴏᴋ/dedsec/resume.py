# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

DYNO_COMMAND = Li.DYNO_COMMAND

@Client.on_message(demon_killer_sigki
                   & senzo_kryo_ni
                   & misa_misa
                   & filters.command("resume", prefixes=DYNO_COMMAND)
                   ) 
async def resume_playing(_, ryui: Message):
    pwn = await ryui.reply_text("Sinxronzasiya olunur @RoBotlarimTg", True) 
    await pwn.edit_text("Serverlə əlaqə yaradılır...") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
    await pwn.delete()  
    hawk = await ryui.reply_text(
            f"**▶️ Dayanan musiqini yenidən başlatdım**",
                                quote=False
                                )
    ded.voice_chatting.resume_playout()
    if ded.msg.get('pause') is not None:
        await ded.msg['pause'].delete()
    await ryui.delete()
    await wait_before_rm((hawk, ryui), Kill_Time)
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
        
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               ☠aykhan_s 😳
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
