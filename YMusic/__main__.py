import importlib
import asyncio
from pytgcalls import idle
from pytgcalls import PyTgCalls
from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES
from YMusic import client, pytgcalls 

loop = asyncio.get_event_loop()


async def init():

    client.start()
    LOGGER("YMusic").info("Account Started Successfully")

    for all_module in ALL_MODULES:
        importlib.import_module("YMusic.plugins" + all_module)

    LOGGER("YMusic.plugins").info("Successfully Imported Modules")
    pytgcalls.start()
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YMusic").info("Stopping YMusic Bot! GoodBye")
