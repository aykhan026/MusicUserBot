
# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMO
   
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

DYNO_COMMAND = Li.DYNO_COMMAND

@Client.on_message(demon_killer_sigki
                   & senzo_kryo_ni
                   & filters.command("group", prefixes=DYNO_COMMAND)
                   )                     
async def list_voice_chat(client, ryui: Message):
    voice_chatting = ded.voice_chatting
    if voice_chatting.is_connected:
        pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
        await pwn.edit_text("Serverlə əlaqə yaradılır...") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")         
        chat_id = int("-100" + str(voice_chatting.full_chat.id))
        await pwn.delete()
        chat = await client.get_chat(chat_id)
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/f52e92e80e10aa7fc294c.jpg",   
            caption=f"👨🏻‍💻 @Ballasresmi\n\nMən olduğum qruplar: \n**{chat.title}**"
            )   
    else:
        hawk = await ryui.reply_text("Hazırda heçbir qrupda oxumuram")
    await wait_before_rm((hawk, ryui), Kill_Time)
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               BOT_RAMO | ramoben200
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 