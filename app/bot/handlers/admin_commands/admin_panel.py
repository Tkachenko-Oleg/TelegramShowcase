from aiogram import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from app.bot.keyboards.admin_menu import admin_panel

import logging


router_admin = Router()


@router_admin.callback_query(lambda callback: callback.data == "callback_admin")
async def admin_handler(callback: CallbackQuery):
    try:
        text = "Панель админа"
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text),
            reply_markup=admin_panel()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
