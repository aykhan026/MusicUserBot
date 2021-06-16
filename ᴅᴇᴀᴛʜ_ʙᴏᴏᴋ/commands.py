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
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

WHITE_COMMAND = Li.WHITE_COMMAND

@Client.on_message(demon_killer_sigki
                   & (senzo_kryo_ni | misa_misa)
                   & filters.command("cmd", prefixes=WHITE_COMMAND)
                   ) 
async def show_help(_, ryui: Message):
    if ded.msg.get('cmd') is not None:
        pwn = await ryui.reply_text("Sinxronzasiya olunur @RoBotlarimTg", True)
        await pwn.edit_text("♻️ Serverlə əlaqə qurulur...")
        await pwn.edit_text("♻️ Yüklənir [░░░░░░              ]")
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░        ]")
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")  
        await pwn.delete()            
        await ded.msg['cmd'].delete()
    ded.msg['cmd'] = hawk = await ryui.reply_photo(
        "https://telegra.ph/file/2e419eca28153982c5e54.jpg",
        caption=FULL_PLAYING_HELP
    )
    await ryui.delete()
    await delete_command_blue((hawk, ryui), CMD_DEL)
    return  
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def delete_command_blue(messages: tuple, delay: int):
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
