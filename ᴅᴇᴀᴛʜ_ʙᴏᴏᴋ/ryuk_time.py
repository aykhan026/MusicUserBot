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
import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li

DYNO_COMMAND = Li.DYNO_COMMAND

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)
self_or_contact_filter = filters.create(
    lambda
    _,
    __,
    ryui:
    (ryui.from_user and ryui.from_user.is_contact) or ryui.outgoing
)
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
@Client.on_message(filters.text
                   & self_or_contact_filter
                   & ~filters.edited
                   & ~filters.via_bot
                   & filters.command("ryuk", prefixes=DYNO_COMMAND)
                   ) 
async def ping_pong(_, ryui: Message):
    start = time()
    pwn = await ryui.reply_text("Syncing with @vrtxmusic", True)
    await pwn.edit_text("and it's servers...")
    await pwn.edit_text("ETR: > sec[░░░░░░              ]")
    await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░        ]")
    await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░░░░░░░░░]")
    delta_ping = time() - start
    hawk = await pwn.edit_text(
        f"""一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]
by~ @mastermindvrtx\n        
**🏻 ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴀɴᴅ ʀᴇᴀᴅʏ ᴛᴏ ᴘʟᴀʏ ɪɴ ᴠᴄ 🏻**:
        `{delta_ping * 1000:.3f}ms`"""
    )
    await delete_ryuk((hawk, ryui), RYUKDEL)
    return
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"

  
async def delete_ryuk(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()   
"""
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
     /  \        /  \        /  \        /  \        /  \        /  \
               ☠爪闩丂ㄒ㠪尺爪工𝓝ᗪᐯ尺ㄒ乂☠
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
""" 
