from aiogram import Bot, Dispatcher
from cprint import cprint
from logging.handlers import TimedRotatingFileHandler
import logging
import asyncio

from app.config import Config
from app.bot.handlers import *
from app.db.create_db import database


bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()
database.create_category_table()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        TimedRotatingFileHandler(
            filename='logger.log',
            when='D',
            interval=1,
            backupCount=7,
            utc=True
        )
    ]
)


async def send_error_to_admin(error_message):
    try:
        for admin_id in Config.ADMIN_IDS:
            await bot.send_message(chat_id=admin_id, text=error_message)
    except Exception as error:
        logging.error(f"An unexpected error occurred while sending the report: {error}")


async def monitor_log_file():
    log_file_path = "logger.log"
    last_position = 0
    while True:
        with open(log_file_path, 'r') as log_file:
            log_file.seek(last_position)
            new_lines = log_file.readlines()
            for line in new_lines:
                if "ERROR" in line:
                    await send_error_to_admin(line.strip())
            last_position = log_file.tell()
        await asyncio.sleep(10)


async def start_bot():
    try:
        cprint.info("Bot is running")
        logging.info("Bot is running")
        dp.include_routers(
            router_start,
            router_help,
            router_home,
            router_about,
            router_contacts,
            router_catalog,
            router_admin,
            router_change_info,
            router_admin_catalog,
            router_get_statistic
        )
        asyncio.create_task(monitor_log_file())
        await dp.start_polling(bot, skip_updates=True)
    finally:
        logging.info("Bot is stopped")
        cprint.err("Bot is stopped")


if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot is stopped: (KeyboardInterrupt or SystemExit)")
        cprint.err("Bot is stopped")
