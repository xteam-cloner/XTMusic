from YMusic.core.bot import YMusicBot, YMusicClient
from .logging import LOGGER
from YMusic.misc import sudo

sudo()

app = YMusicClient
call = YMusicBot
#YMusicBot = Call()

# Access the PyTgCalls instance and Client from the Call object
#YMusicUser = YMusicBot.pytgcalls
#YMusicClient = YMusicBot.client
