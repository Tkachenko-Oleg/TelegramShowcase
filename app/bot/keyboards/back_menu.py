from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def back_menu():
    buttons = [
        [InlineKeyboardButton(text="Главное меню", callback_data="callback_home")]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
