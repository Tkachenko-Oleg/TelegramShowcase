from aiogram import Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import admin_panel, show_back_button, clear_keyboard
from app.bot.states.admin_states import AdminStates
from app.tools import update_info

import logging


router_change_info = Router()


@router_change_info.callback_query(lambda callback: callback.data == "change_info")
async def await_new_info(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.answer("Напишите новое описание", reply_markup=show_back_button())
        await state.set_state(AdminStates.change_info)
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_change_info.message(AdminStates.change_info)
async def change_info(message: Message, state: FSMContext):
    try:
        if message.text:
            text = "Описание не обновлено"
            if message.text != "Отмена":
                update_info(message.text)
                text = "Описание обновлено"
            await message.answer(text=text, reply_markup=clear_keyboard())
            await message.answer_photo(
                photo=FSInputFile("app/images/brand/logo.png"),
                caption="Панель админа",
                reply_markup=admin_panel()
            )
            await state.clear()
        else:
            await message.answer("Ошибка. Отправьте текстовое сообщение")
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
