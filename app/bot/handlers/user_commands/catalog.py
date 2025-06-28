from aiogram import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext

from app.tools import change_image, correct_page
from app.bot.keyboards import catalog_keyboard, viewer_keyboard

import logging


router_catalog = Router()


@router_catalog.callback_query(lambda callback: callback.data == "callback_catalog")
async def catalog_handler(callback: CallbackQuery):
    try:
        text = "Каталог"
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text),
            reply_markup=catalog_keyboard()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_catalog.callback_query(lambda callback: callback.data.startswith("category_"))
async def viewer_handler(callback: CallbackQuery, state: FSMContext):
    try:
        data = {
            "category": callback.data,
            "page": 1
        }
        await state.update_data(data=data)

        try:
            img_path = change_image(callback.data, 1)
            await callback.message.edit_media(
                media=InputMediaPhoto(media=FSInputFile(img_path)),
                reply_markup=viewer_keyboard(callback.data, 1)
            )
        except IndexError:
            img = FSInputFile("app/images/brand/logo.png")
            await callback.message.edit_media(
                media=InputMediaPhoto(media=img, caption="На данный момент категория пустая"),
                reply_markup=viewer_keyboard(callback.data, 0)
            )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_catalog.callback_query(lambda callback: callback.data == "page_number")
async def page_number_clicked(callback: CallbackQuery):
    try:
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_catalog.callback_query(lambda callback: callback.data in ["prev_page", "next_page"])
async def change_page(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        category = data.get("category")
        page = data.get("page")
        if callback.data == "prev_page":
            new_page = correct_page(category, page - 1)
        else:
            new_page = correct_page(category, page + 1)
        if new_page != page and new_page > 0:
            new_data = {
                "category": category,
                "page": new_page
            }
            await state.update_data(data=new_data)

            img_path = change_image(category, new_page)
            await callback.message.edit_media(
                media=InputMediaPhoto(media=FSInputFile(img_path)),
                reply_markup=viewer_keyboard(category, new_page)
            )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
