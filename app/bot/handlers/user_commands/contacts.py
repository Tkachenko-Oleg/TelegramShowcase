from aiogram import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from app.bot.keyboards.back_menu import back_menu
from app.config import Config

import logging

router_contacts = Router()


@router_contacts.callback_query(lambda callback: callback.data == "callback_contacts")
async def contacts_handler(callback: CallbackQuery):
    try:
        text = (
            "Контактная информация\n\n"
            f"Наш Telegram: {Config.TELEGRAM_LINK}\n"
            f"Наш WhatsApp: [ссылка]({Config.WHATSAPP_LINK})\n"
            f"Наш VK: [ссылка]({Config.VK_LINK})\n"
            f"Наша почта: {Config.MAIL_LINK}\n"
            f"Наш номер телефона: {Config.PHONE_NUMBER}"
        )
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text, parse_mode="MarkdownV2"),
            reply_markup=back_menu()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
