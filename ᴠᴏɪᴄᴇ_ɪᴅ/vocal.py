
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
import ffmpeg
import asyncio
from datetime import datetime
from pyrogram import emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
from pyrogram.types import Message
from pytgcalls import GroupCall
from ɴᴏᴛᴇʙᴏᴏᴋ.design_i import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


class DeathCharm(object):
    def __init__(self):
        self.voice_chatting = GroupCall(None, path_to_log_file='')
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}

    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )

    async def send_playlist(self):
        playlist = self.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY}**Nothing is the playlist**"
        else:
            if len(playlist) == 1:
                pl = f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n🦋ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ🦋
✨ŇỖŴ_ƤĹÃЎĮŇĞ✨:-\n
"""
            else:
                pl = f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n🦋ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ🦋
✨ŇỖŴ_ƤĹÃЎĮŇĞ✨:-\n
"""
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}({x.link})**"
                for i, x in enumerate(playlist)
            ])
        if self.msg.get('playlist') is not None:
            await self.msg['playlist'].delete()
        self.msg['playlist'] = await self.send_text(pl)

    async def skip_current_playing(self):
        voice_chatting = self.voice_chatting
        playlist = self.playlist
        if not playlist:
            return
        if len(playlist) == 1:
            await self.update_start_time()
            return
        client = voice_chatting.client
        raw_hug = os.path.join(client.workdir, fmedaddyy)
        voice_chatting.input_filename = os.path.join(
            raw_hug,
            f"{playlist[1].audio.file_unique_id}.raw"
        )
        await self.update_start_time()
        # remove old track from playlist
        old_track = playlist.pop(0)
        print(f"- START PLAYING: {playlist[0].audio.title}")
        await self.send_playlist()
        os.remove(os.path.join(
            raw_hug,
            f"{old_track.audio.file_unique_id}.raw")
        )
        if len(playlist) == 1:
            return
        await self.download_audio(playlist[1])

    async def send_text(self, text):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        chat_id = self.chat_id
        message = await client.send_message(
            chat_id,
            text,
            disable_web_page_preview=True,
            disable_notification=True
        )
        return message

    async def download_audio(self, ryui: Message):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        raw_file = os.path.join(client.workdir, fmedaddyy,
                                f"{ryui.audio.file_unique_id}.raw")
        if not os.path.isfile(raw_file):
            original_file = await ryui.download()
            ffmpeg.input(original_file).output(
                raw_file,
                format='s16le',
                acodec='pcm_s16le',
                ac=2,
                ar='48k',
                loglevel='error'
            ).overwrite_output().run()
            os.remove(original_file)
ded = DeathCharm()
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


@ded.voice_chatting.on_network_status_changed
async def network_status_changed_handler(ip: GroupCall, is_connected: bool):
    if is_connected:
        ded.chat_id = int("-100" + str(ip.full_chat.id))
        hawk = await ded.send_text(
            f"[🦋]一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋]\n"
            "          .𝕆ℕ𝕃𝕀ℕ𝔼🟢.\n"
            )     
        await delete_switch_on((hawk,), SWITCH_ON_TIME)              
    else:
        hawk = await ded.send_text(
            f"[🦋]一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋]\n"     
            "  .🔇𝕀𝔻𝕃𝔼_𝕄𝕆𝔻𝔼_𝔸ℂ𝕋𝕀𝕍𝔼🔇.\n"
            )       
        await delete_switch_off((hawk,), SWITCH_OFF_TIME)                       
        ded.chat_id = None
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def delete_switch_on(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()

async def delete_switch_off(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


@ded.voice_chatting.on_playout_ended
async def playout_ended_handler(_, __):
    await ded.skip_current_playing()


"""
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
     /  \        /  \        /  \        /  \        /  \        /  \
               ☠爪闩丂ㄒ㠪尺爪工𝓝ᗪᐯ尺ㄒ乂☠
__/        \__/        \__/        \__/        \__/        \__/       
  \        /  \        /  \        /  \        /  \        /  \       
     \__/        \__/        \__/        \__/        \__/        \__/
""" 