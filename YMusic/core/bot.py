from pyrogram import Client
from pytgcalls import PyTgCalls
import config
from ..logging import LOGGER

class Call:
    def __init__(self):
        self.client = None
        self.pytgcalls = None
        try:
            self.client = Client(
                name="AnonXAss1",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.SESSION_STRING),
            )
            self.pytgcalls = PyTgCalls(
                self.client,
                cache_duration=100,
            )
            LOGGER.info("YMusicBot berhasil diinisialisasi.")
        except ValueError as ve:
            LOGGER.error(f"Nilai konfigurasi tidak valid: {ve}")
            raise  # Re-raise exception untuk penanganan lebih lanjut
        except Exception as e:
            LOGGER.error(f"Gagal menginisialisasi YMusicBot: {e}")
            raise  # Re-raise exception untuk penanganan lebih lanjut

    def get_client(self):
        return self.client

    def get_pytgcalls(self):
        return self.pytgcalls

# Instantiate the Call class
try:
    YMusicBot = Call()
    YMusicUser = YMusicBot.get_pytgcalls()
    YMusicClient = YMusicBot.get_client()
except Exception as init_error:
    LOGGER.critical(f"YMusicBot gagal diinisialisasi secara kritis: {init_error}")
    YMusicBot = None
    YMusicUser = None
    YMusicClient = None

if YMusicBot:
    LOGGER.info("YMusicBot siap digunakan.")
else:
    LOGGER.critical("YMusicBot tidak dapat diinisialisasi. Periksa konfigurasi dan log untuk detailnya.")

