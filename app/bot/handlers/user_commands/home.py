from aiogram import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from app.bot.keyboards.main_menu import main_keyboard, admin_main_keyboard
from app.tools.is_admin import is_admin

import logging


router_home = Router()


@router_home.callback_query(lambda callback: callback.data == "callback_home")
async def home_handler(callback: CallbackQuery):
    try:
        text = "Главное меню"
        img = FSInputFile("app/images/brand/logo.png")
        keyboard = admin_main_keyboard() if is_admin(callback.from_user.id) else main_keyboard()
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text),
            reply_markup=keyboard
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
