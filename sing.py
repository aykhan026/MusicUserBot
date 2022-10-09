# Ballasresmi - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @BOT_RAMO

import os
import asyncio
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li

WHITE_COMMAND = Li.WHITE_COMMAND

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
@Client.on_message(
    filters.group
    & ~filters.edited
    & misa_misa
    & (filters.command("sing", prefixes=WHITE_COMMAND) | filters.audio)        
)
async def play_track(client, ryui: Message):
    voice_chatting = ded.voice_chatting
    playlist = ded.playlist
    # check audio
    if ryui.audio:
        if ryui.audio.duration > (Auto_Add2Play_TimeM * 60):
            pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
            await pwn.edit_text("Serverlə əlaqə yaradılır...") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
            await pwn.delete()                   
            hawk = await ryui.reply_text(
                f"{emoji.ROBOT} Bu musiqini qoşa bilmirəm"
                f"{str(Auto_Add2Play_TimeM)} dəqiqəlik musiqilərə icazə verilir"
                "**Başka musiqi yoxlayın**\n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
        media_aud = ryui
    elif ryui.reply_to_message and ryui.reply_to_message.audio:
        media_aud = ryui.reply_to_message
        if media_aud.audio.duration > (Kill_Hour * 60 * 60):
            pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
            await pwn.edit_text("Serverlə əlaqə yaradılır...") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
            await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
            await pwn.delete()           
            hawk = await ryui.reply_text(
                f"{emoji.ROBOT} Xəta"
                f"{str(Kill_Hour)} Saatlıq musiqini qoşa bilmirəm \n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
    else:
        await ded.send_playlist()
        await ryui.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == media_aud.audio.file_unique_id:
        hawk = await ryui.reply_text(f"**❗ Bu musiqi onsuzda playlistdə var**"
                                    )
        await wait_before_rm((hawk, ryui), Kill_Time)
        return
    # add to playlist
    playlist.append(media_aud)
    if len(playlist) == 1:
        pwn = await ryui.reply_text("Sinxronzasiya olunur @Ballasresmi", True) 
        await pwn.edit_text("Serverlə əlaqə yaradılır...") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░ ]") 
        await pwn.edit_text("♻️ Yüklənir [░░░░░░░░░░░░░░░░░░░░]")
        await pwn.delete() 
        m_status = await ryui.reply_text(
            f"**Musiqini qoşuram səbirli olun**"
        )
        await ded.download_audio(playlist[0])
        voice_chatting.input_filename = os.path.join(
            client.workdir,
            fmedaddyy,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await ded.update_start_time()
        await m_status.delete()
        print(f"- Oxunan: {playlist[0].audio.title}")
    await ded.send_playlist()
    for track in playlist[:2]:
        await ded.download_audio(track)
    if not ryui.audio:
        await ryui.delete()
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
             🤦🏻‍♂️   BOT_RAMO☠
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
""