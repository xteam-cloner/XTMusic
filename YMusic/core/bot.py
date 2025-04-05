from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from ..logging import LOGGER


class Call:
    def __init__(self):
        try:
            self.client = Client(
                name="AnonXAss1",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING1),
            )
            self.pytgcalls = PyTgCalls(
                self.client,
                cache_duration=100,
            )
            LOGGER.info("YMusicBot berhasil diinisialisasi.")
        except Exception as e:
            LOGGER.error(f"Gagal menginisialisasi YMusicBot: {e}")
            raise  # Re-raise exception untuk penanganan lebih lanjut jika diperlukan

# Instantiate the Call class
YMusicBot = Call()

# Access the PyTgCalls instance and Client from the Call object
YMusicUser = YMusicBot.pytgcalls
YMusicClient = YMusicBot.client
