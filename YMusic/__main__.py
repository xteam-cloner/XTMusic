import importlib
import asyncio
import config
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES
from YMusic import client, pytgcalls

async def init():
    await client .start()
    for all_module in ALL_MODULES:
        importlib.import_module("YMusic.plugins" + all_module)
    LOGGER("YMusic.plugins").info("Successfully Imported Modules...")
    await client.start()
    await pytgcalls.start()
    try:
        await pytgcalls.stream_call("https://telegra.ph/file/cba632240b79207bf8a9c.mp4")
    except NoActiveGroupCall:
        exit()
    except:
        pass
    await idle()
    await client.stop()
    await pytgcalls.stop()
    LOGGER("YMusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())    
