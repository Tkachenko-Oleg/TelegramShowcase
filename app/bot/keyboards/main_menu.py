from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="📁 Каталог", callback_data="callback_catalog"),
            InlineKeyboardButton(text="📞 Контакты", callback_data="callback_contacts")
        ],
        [
            InlineKeyboardButton(text="ℹ️ Обо мне", callback_data="callback_about"),
            InlineKeyboardButton(text="❓ Помощь", callback_data="callback_help")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def admin_main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="📁 Каталог", callback_data="callback_catalog"),
            InlineKeyboardButton(text="📞 Контакты", callback_data="callback_contacts")
        ],
        [
            InlineKeyboardButton(text="ℹ️ Обо мне", callback_data="callback_about"),
            InlineKeyboardButton(text="❓ Помощь", callback_data="callback_help")
        ],
        [
            InlineKeyboardButton(text="⚙️ Админ", callback_data="callback_admin")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
