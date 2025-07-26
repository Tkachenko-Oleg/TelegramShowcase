from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def admin_panel():
    buttons = [
        [InlineKeyboardButton(text="Изменить Каталог", callback_data="change_catalog")],
        [InlineKeyboardButton(text="Изменить Описание", callback_data="change_info")],
        [InlineKeyboardButton(text="Статистика", callback_data="callback_statistic")],
        [InlineKeyboardButton(text="Главное меню", callback_data="callback_home")]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
