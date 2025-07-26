from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def choose_period_keyboard():
    buttons = [
        [KeyboardButton(text="Сегодня")],
        [KeyboardButton(text="Вчера")],
        [KeyboardButton(text="Неделя")],
        [KeyboardButton(text="Месяц")],
        [KeyboardButton(text="3 месяца")],
        [KeyboardButton(text="6 месяцев")],
        [KeyboardButton(text="Назад")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard


def clear_keyboard():
    return ReplyKeyboardRemove()
