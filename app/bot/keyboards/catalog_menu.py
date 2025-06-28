from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from json import load


def catalog_keyboard():
    with open("app/path_provider.json") as file:
        data = load(file)
    categories = list(data.get('catalog').keys())
    buttons = [[
        InlineKeyboardButton(
            text=data["catalog"][categories[0]]["title"],
            callback_data=f"{categories[0]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[1]]["title"],
            callback_data=f"{categories[1]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[2]]["title"],
            callback_data=f"{categories[2]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[3]]["title"],
            callback_data=f"{categories[3]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[4]]["title"],
            callback_data=f"{categories[4]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[5]]["title"],
            callback_data=f"{categories[5]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[6]]["title"],
            callback_data=f"{categories[6]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[7]]["title"],
            callback_data=f"{categories[7]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[8]]["title"],
            callback_data=f"{categories[8]}"
        )
    ], [InlineKeyboardButton(text="Назад", callback_data="callback_home")]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def admin_catalog_keyboard():
    with open("app/path_provider.json") as file:
        data = load(file)
    categories = list(data.get('catalog').keys())
    buttons = [[
        InlineKeyboardButton(
            text=data["catalog"][categories[0]]["title"],
            callback_data=f"admin_{categories[0]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[1]]["title"],
            callback_data=f"admin_{categories[1]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[2]]["title"],
            callback_data=f"admin_{categories[2]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[3]]["title"],
            callback_data=f"admin_{categories[3]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[4]]["title"],
            callback_data=f"admin_{categories[4]}"
        ),
        InlineKeyboardButton(
            text=data["catalog"][categories[5]]["title"],
            callback_data=f"admin_{categories[5]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[6]]["title"],
            callback_data=f"admin_{categories[6]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[7]]["title"],
            callback_data=f"admin_{categories[7]}"
        )
    ], [
        InlineKeyboardButton(
            text=data["catalog"][categories[8]]["title"],
            callback_data=f"admin_{categories[8]}"
        )
    ], [InlineKeyboardButton(text="Назад", callback_data="callback_home")]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
