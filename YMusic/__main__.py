import importlib
import asyncio
import config
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES
from YMusic import client, pytgcalls

async def start_services():
    try:
        await client.start()
        for all_module in ALL_MODULES:
            importlib.import_module("YMusic.plugins." + all_module)
        LOGGER("YMusic.plugins").info("Successfully Imported Modules...")
        await pytgcalls.start()

        try:
            await pytgcalls.stream_call("https://telegra.ph/file/cba632240b79207bf8a9c.mp4")
            LOGGER("YMusic").info("Started Streaming Video Call")
        except NoActiveGroupCall:
            LOGGER("YMusic").error("No Active Group Call Found.")
            await stop_services() # Stop services if no active group call.
            return
        except Exception as e:
            LOGGER("YMusic").error(f"Error starting video call: {e}")
            await stop_services() # Stop services if other error.
            return

        await idle()
    except Exception as e:
        LOGGER("YMusic").error(f"An error occurred during startup: {e}")
        await stop_services() # Stop services if startup error.
    finally:
        # stop_services will be called in any case, even if idle is interrupted.
        pass

async def stop_services():
    try:
        if client.start: #Add check for client connection.
            await client.stop()
        if pytgcalls.start: #Add check for pytgcalls connection.
            await pytgcalls.stop()
        LOGGER("YMusic").info("Services Stopped.")
        LOGGER("YMusic").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝐂𝐡𝐢𝐧𝐧𝐚 ♨️\n╚═════ஜ۩۞۩ஜ════╝")
    except Exception as e:
        LOGGER("YMusic").error(f"An error occurred during shutdown: {e}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_services())
