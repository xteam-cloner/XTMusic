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
            def get_client(self):
                return self.client
                
                def get_pytgcalls(self):
                    return self.pytgcalls
                    
                    try:
                        YMusicBot = YMusicUser = YMusicClient = None
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    finally:
                        print ("Finishing")
