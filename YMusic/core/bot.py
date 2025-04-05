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
            LOGGER(__name__).info("PyTgCalls client initialized successfully.") # Better logging.

        except Exception as e:
            LOGGER(__name__).error(f"Failed to initialize PyTgCalls: {e}")
            self.client = None
            self.pytgcalls = None

        try:
            self.YMusicBot = None # corrected from YMusicBot = YMusicUser = YMusicClient = None
            self.YMusicUser = None
            self.YMusicClient = None

        except Exception as e:
            LOGGER(__name__).error(f"Error initializing YMusic variables: {e}")

        finally:
            LOGGER(__name__).info("Call class initialization finished.")

    def get_client(self):
        return self.client

    def get_pytgcalls(self):
        return self.pytgcalls

call_instance = Call()

if call_instance.get_client() and call_instance.get_pytgcalls():
    # PyTgCalls dan Client berhasil diinisialisasi
    client = call_instance.get_client()
    pytgcalls = call_instance.get_pytgcalls()
    # Lanjutkan dengan menggunakan client dan pytgcalls
else:
    # Inisialisasi gagal
    print("Failed to initialize PyTgCalls.")

# You can access the YMusic variables like this:
print(call_instance.YMusicBot)
