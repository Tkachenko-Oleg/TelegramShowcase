from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from app.bot.keyboards.main_menu import main_keyboard, admin_main_keyboard
from app.tools.is_admin import is_admin

import logging


router_start = Router()


@router_start.message(Command("start"))
async def start_handler(message: Message):
    try:
        keyboard = admin_main_keyboard() if is_admin(message.from_user.id) else main_keyboard()
        await message.answer_photo(
            photo=FSInputFile("app/images/brand/logo.png"),
            caption="Главное меню",
            reply_markup=keyboard
        )
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
