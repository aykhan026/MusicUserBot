
# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMO

from pyrogram import filters, emoji
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def misa_misa_filter(
    _,
    __,
    ryui: Message):
    voice_chatting = ded.voice_chatting
    if not voice_chatting.is_connected:
        return False
    chat_id = int("-100" + str(voice_chatting.full_chat.id))
    if ryui.chat.id == chat_id:
        return True
    return False
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


misa_misa = filters.create(
    misa_misa_filter
    )

"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
               BOT_RAMO
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
"""