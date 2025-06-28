from aiogram import Router
from aiogram.types import CallbackQuery,  InputMediaPhoto, FSInputFile

from app.bot.keyboards.back_menu import back_menu
from app.config import Config

import logging


router_help = Router()


@router_help.callback_query(lambda callback: callback.data == "callback_help")
async def help_handler(callback: CallbackQuery):
    try:
        text = (
            f"Если возникли вопросы, обратитесь сюда:\n"
            f"{Config.MAIL_LINK}"
        )
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text, parse_mode="MarkdownV2"),
            reply_markup=back_menu()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
