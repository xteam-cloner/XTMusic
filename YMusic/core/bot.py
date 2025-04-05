from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from ..logging import LOGGER

class YMusicBot:
    def __init__(self):
        try:
            YMusicUser = Client(
                name="AnonXAss1",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING1),
            )
            self.PyTgCalls(
                self.YMusicUser,
                cache_duration=100,
            )
            
            LOGGER.info("YMusicBot berhasil diinisialisasi.")
        except Exception as e:
            LOGGER.error(f"Gagal menginisialisasi YMusicBot: {e}")
            raise  # Re-raise exception untuk penanganan lebih lanjut jika diperlukan

YMusicUser = PyTgCalls(YMusicBot)
