# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s

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
                   & filters.command("pause", prefixes=DYNO_COMMAND)
                   ) 
async def pause_playing(_, ryui: Message):
    pwn = await ryui.reply_text("Sinxronzasiya olunur @RoBotlarimTg", True) 
    await pwn.edit_text("Serverlə əlaqə yaradılır...") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
    await pwn.delete() 
    ded.voice_chatting.pause_playout()
    await ded.update_start_time(reset=True)
    hawk = await ryui.reply_text(
            f"⏸️ **Musiqini müvəqqəti dayandırdım**"
          )
    ded.msg['pause'] = hawk
    await ryui.delete()
    
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               aykhan_s
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
