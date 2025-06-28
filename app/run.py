from cprint import cprint
import asyncio

from app.bot.main import start_bot


async def main():
    cprint.info("System is running")
    await asyncio.gather(start_bot())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        cprint.err("System is stopped")
