
# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMO
 
import asyncio
from pyrogram import Client, filters
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
                   & filters.command("replay", prefixes=DYNO_COMMAND)
                   ) 
async def restart_playing(_, ryui: Message):
    voice_chatting = ded.voice_chatting
    if not ded.playlist:
        return

    pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
    await pwn.edit_text("Serverlə əlaqə yaradılır...") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
    await pwn.delete()
    await ryui.reply_text(
            f"🔁 **Musiqini yenidən başlatdım**"
            )
    voice_chatting.restart_playout()
    await ded.update_start_time()           
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               ☠BOT_RAMO )))☠
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
"""