import json
from aiogram import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from app.bot.keyboards.back_menu import back_menu

import logging


router_about = Router()


@router_about.callback_query(lambda callback: callback.data == "callback_about")
async def about_handler(callback: CallbackQuery):
    try:
        with open("app/path_provider.json") as file:
            data = json.load(file)
        text = data["description"]
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text),
            reply_markup=back_menu()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
