# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s

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
    pwn = await ryui.reply_text("Sinxronzasiya olunur @RoBotlarimTg", True)
    await pwn.edit_text("Serverlə əlaqə qurulur...")
    await pwn.edit_text("♻️ Yüklənir [░░░░░░              ]")
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░        ]")
    await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
    delta_ping = time() - start
    hawk = await pwn.edit_text(
        f"""**LEDY MUSİC**\n        
**Bəli, Mən aktivəm**:
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
  🇦🇿👉   \  aykhan_s \  bu tağı hələ çox yerdə görəcəksiniz...) /
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
""" 
