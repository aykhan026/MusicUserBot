"""
     /  \        /  \        /  \        /  \        /  \        /  \
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
            𝔻𝕠𝕟❜𝕥 𝕂𝕒𝕟𝕘 𝕋𝕙𝕖 ℝ𝕖𝕡𝕠 𝕨𝕚𝕥𝕙𝕠𝕦𝕥 𝕤𝕥𝕒𝕣𝕚𝕟𝕘 𝕒𝕟𝕕 𝕗𝕠𝕣𝕜𝕚𝕟𝕘...     
                        🅼🅰🆂🆃🅴🆁🅼🅸🅽🅳🆅🆁🆃🆇    
     /  \        /  \        /  \        /  \        /  \        /  \
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
"""   
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
        pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[░░░░░░              ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░        ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░░░░░░░░░]") 
        await pwn.delete()            
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg",
            caption="[🦋]**ɴᴏᴛʜɪɴɢ ɪꜱ ɪɴ ᴘʟᴀʏʟɪꜱᴛ ʏᴇᴛ!**[🦋]"
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
               ☠爪闩丂ㄒ㠪尺爪工𝓝ᗪᐯ尺ㄒ乂☠
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""" 
