from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def show_back_button():
    buttons = [
        [KeyboardButton(text="Отмена")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def clear_keyboard():
    return ReplyKeyboardRemove()
