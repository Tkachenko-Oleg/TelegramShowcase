from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from json import load


def viewer_keyboard(category: str, page: int):
    with open("app/path_provider.json") as file:
        data = load(file)
        length = len(data["catalog"][category].values()) - 1

    prev_button = InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_page")
    next_button = InlineKeyboardButton(text="Далее ➡️", callback_data="next_page")
    page_button = InlineKeyboardButton(text=f"{page}/{length}", callback_data="page_number")
    contact_button = InlineKeyboardButton(text="📞 Контакты", callback_data="callback_contacts")
    back_button = InlineKeyboardButton(text="📁 Каталог", callback_data="callback_catalog")

    buttons = [
        [prev_button, page_button, next_button],
        [back_button, contact_button]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def admin_viewer_keyboard(category: str, page: int):
    category = category.replace("admin_", "")
    with open("app/path_provider.json") as file:
        data = load(file)
        length = len(data["catalog"][category].values()) - 1

    prev_button = InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_prev_page")
    next_button = InlineKeyboardButton(text="Далее ➡️", callback_data="admin_next_page")
    page_button = InlineKeyboardButton(text=f"{page}/{length}", callback_data="page_number")
    add_button = InlineKeyboardButton(text="Добавить ➕", callback_data="add_item")
    delete_button = InlineKeyboardButton(text="Удалить 🗑", callback_data="delete_item")
    back_button = InlineKeyboardButton(text="📁 Каталог", callback_data="change_catalog")

    buttons = [
        [prev_button, page_button, next_button],
        [delete_button, add_button],
        [back_button]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
