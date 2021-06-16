# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s
   
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
        pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[░░░░░░              ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░        ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░░░░░░░░░]")         
        chat_id = int("-100" + str(voice_chatting.full_chat.id))
        await pwn.delete()
        chat = await client.get_chat(chat_id)
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/2e419eca28153982c5e54.jpg",   
            caption=f"[🦋]一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋]\n\nᴄᴜʀʀᴇɴᴛʟʏ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏꜰ: \n**{chat.title}**"
            )   
    else:
        hawk = await ryui.reply_text("⏳ᴡᴀɪᴛɪɴɢ ᴛᴏ ʙᴇ ᴘʟᴜɢɢᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ⌛️")
    await wait_before_rm((hawk, ryui), Kill_Time)
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               ☠爪闩丂ㄒ㠪尺爪工𝓝ᗪᐯ尺ㄒ乂☠
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
