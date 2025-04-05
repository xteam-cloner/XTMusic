import importlib
import asyncio
from pytgcalls import idle
from pytgcalls import PyTgCalls
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

        await pytgcalls.start()
        await idle()

    except Exception as e:
        LOGGER("YMusic").critical(f"Initialization failed: {e}")
        await client.stop()
        await pytgcalls.stop()
        return

async def main():
    try:
        await init()
    except KeyboardInterrupt:
        LOGGER("YMusic").info("Stopping YMusic Bot due to KeyboardInterrupt! GoodBye")
    except Exception as e:
        LOGGER("YMusic").critical(f"An unexpected error occurred: {e}")
    finally:
        LOGGER("YMusic").info("Stopping YMusic Bot! GoodBye")
        await client.stop()
        await pytgcalls.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
