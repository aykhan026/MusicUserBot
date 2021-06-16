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
from pyrogram import Client, filters
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
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
                   & filters.command("raw", prefixes=DYNO_COMMAND)
                   ) 
async def clean_raw_pcm(client, ryui: Message):
    raw_hug = os.path.join(client.workdir, fmedaddyy)
    all_fn: list[str] = os.listdir(raw_hug)
    for track in ded.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    files = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                files += 1
                os.remove(os.path.join(raw_hug, fn))             
    hawk = await ryui.reply_text(
        f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n ɴᴜᴍʙᴇʀ ᴏꜰ ᴄʟᴇᴀɴᴇᴅ ᴛᴇᴍᴘ ꜰɪʟᴇ: **{files}**"
                    )
    await ryui.delete()
    await wait_before_rm((hawk, ryui), Kill_Time)
    return
    
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
