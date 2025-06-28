from aiogram import Router
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext

from app.tools import change_image, correct_page, delete_item, save_item, is_correct_item
from app.bot.keyboards import admin_catalog_keyboard, admin_viewer_keyboard, show_back_button, clear_keyboard
from app.bot.states.admin_states import AdminStates

import logging


router_admin_catalog = Router()


@router_admin_catalog.callback_query(lambda callback: callback.data == "change_catalog")
async def admin_catalog(callback: CallbackQuery):
    try:
        text = "Каталог (админ)"
        img = FSInputFile("app/images/brand/logo.png")
        await callback.message.edit_media(
            media=InputMediaPhoto(media=img, caption=text),
            reply_markup=admin_catalog_keyboard()
        )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.callback_query(lambda callback: callback.data.startswith("admin_category_"))
async def admin_viewer_handler(callback: CallbackQuery, state: FSMContext):
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
                reply_markup=admin_viewer_keyboard(callback.data, 1)
            )
        except IndexError:
            img = FSInputFile("app/images/brand/logo.png")
            await callback.message.edit_media(
                media=InputMediaPhoto(media=img, caption="Категория пустая"),
                reply_markup=admin_viewer_keyboard(callback.data, 0)
            )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.callback_query(lambda callback: callback.data == "page_number")
async def page_number_clicked(callback: CallbackQuery):
    try:
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.callback_query(lambda callback: callback.data in ["admin_prev_page", "admin_next_page"])
async def change_page(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        category = data.get("category")
        page = data.get("page")
        if callback.data == "admin_prev_page":
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
                reply_markup=admin_viewer_keyboard(category, new_page)
            )
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.callback_query(lambda callback: callback.data == "add_item")
async def add_item_handler(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.answer(
            text="Напишите название файла\n(без пробелов, точек, спец.символов и без разширений)",
            reply_markup=show_back_button()
        )
        await state.set_state(AdminStates.get_filename)
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.message(AdminStates.get_filename)
async def get_filename(message: Message, state: FSMContext):
    try:
        if message.text and message.text.lower() == "отмена":
            await message.answer(
                text="Элемент не добавлен",
                reply_markup=clear_keyboard()
            )
            await message.answer_photo(
                photo=FSInputFile("app/images/brand/logo.png"),
                caption="Каталог (админ)",
                reply_markup=admin_catalog_keyboard()
            )
            await state.clear()
        elif message.text and message.text.lower() != "отмена":
            data = await state.get_data()
            category = data.get('category')
            absolute_path = f"app/images/catalog/{message.text}.png"
            if is_correct_item(category=category, new_element_path=absolute_path):
                await state.update_data(filename=message.text)
                await state.set_state(AdminStates.get_file)
                await message.answer(
                    text="Отправьте файл (фото)",
                    reply_markup=show_back_button()
                )
            else:
                await message.answer("Ошибка. Имя файла занято")
        else:
            await message.answer("Ошибка. Отправьте текстовое сообщение")
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.message(AdminStates.get_file)
async def get_file(message: Message, state: FSMContext):
    try:
        if message.text and message.text.lower() == "отмена":
            await message.answer(
                text="Элемент не добавлен",
                reply_markup=clear_keyboard()
            )
            await message.answer_photo(
                photo=FSInputFile("app/images/brand/logo.png"),
                caption="Каталог (админ)",
                reply_markup=admin_catalog_keyboard()
            )
            await state.clear()
        elif message.photo:
            from app.bot.main import bot

            data = await state.get_data()
            category = data.get('category')
            filename = data.get('filename')
            absolute_path = f"app/images/catalog/{filename}.png"
            photo_id = message.photo[-1].file_id
            file = await bot.get_file(photo_id)
            await bot.download_file(
                file_path=file.file_path,
                destination=absolute_path
            )
            save_item(category, absolute_path)
            await message.answer(
                text="Элемент добавлен",
                reply_markup=clear_keyboard()
            )
            await message.answer_photo(
                photo=FSInputFile("app/images/brand/logo.png"),
                caption="Каталог (админ)",
                reply_markup=admin_catalog_keyboard()
            )
            await state.clear()
        else:
            await message.answer("Ошибка. Отправьте фото")
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_admin_catalog.callback_query(lambda callback: callback.data == "delete_item")
async def delete_item_handler(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        category = data.get("category")
        page = data.get("page")
        try:
            delete_item(category, page)
            new_page = correct_page(category, page - 1)
            if new_page > 0:
                new_data = {
                    "category": category,
                    "page": new_page
                }
                await state.update_data(data=new_data)
                img_path = change_image(category, new_page)
                await callback.message.edit_media(
                    media=InputMediaPhoto(media=FSInputFile(img_path)),
                    reply_markup=admin_viewer_keyboard(category, new_page)
                )
                await callback.answer("Элемент удален")
            else:
                img = FSInputFile("app/images/brand/logo.png")
                await callback.message.edit_media(
                    media=InputMediaPhoto(media=img, caption="Категория пустая"),
                    reply_markup=admin_viewer_keyboard(category, 0)
                )
                await callback.answer()
        except IndexError:
            await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
