
# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMO

import os
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from pytgcalls import GroupCall
from datetime import datetime, timedelta
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
                   & filters.command("mutevc", prefixes=DYNO_COMMAND)
                   ) 
async def mute(client, ryui: Message):
    voice_chatting = ded.voice_chatting  
    chat_id = int("-100" + str(voice_chatting.full_chat.id))  
    chat = await client.get_chat(chat_id)    
    voice_chatting.set_is_mute(True)
    hawk = await ryui.reply_photo(
            "https://telegra.ph/file/f52e92e80e10aa7fc294c.jpg",   
            caption=f"**🔇 Səssizə alındım {chat.title}**"
            )              
    await delay_mute_tm((hawk, ryui), Kill_Time)  
    

async def delay_mute_tm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               BOT_RAMO
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 