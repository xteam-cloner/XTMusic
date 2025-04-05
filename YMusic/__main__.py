import importlib
import asyncio
from pyrogram import idle
from pytgcalls import NoActiveGroupCall
from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES
from YMusic import client, pytgcalls

async def init():
    try:
        await client.start()
        LOGGER("YMusic").info("Account Started Successfully")

        for module_name in ALL_MODULES:
            try:
                importlib.import_module(f"YMusic.plugins.{module_name}")
                LOGGER("YMusic.plugins").info(f"Successfully Imported module: {module_name}")
            except ImportError as e:
                LOGGER("YMusic.plugins").error(f"Failed to import module {module_name}: {e}")

        await client.start()
        await pytgcalls.start()
    try:
        await pytgcalls.stream_call("https://telegra.ph/file/cba632240b79207bf8a9c.mp4")
    except NoActiveGroupCall:
        LOGGER("AnonXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
        await idle()
        await client.stop()
        await pytgcalls.stop()
        LOGGER("YMusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")
        
        if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
