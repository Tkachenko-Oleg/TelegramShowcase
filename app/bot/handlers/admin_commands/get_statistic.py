from aiogram import Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from app.bot.keyboards.period_statistic import choose_period_keyboard, clear_keyboard
from app.bot.keyboards.admin_menu import admin_panel
from app.tools.visualization_analytics import visualization_analytics, delete_tmp_image
from app.bot.states.admin_states import AdminStates

import logging


router_get_statistic = Router()


@router_get_statistic.callback_query(lambda callback: callback.data == "callback_statistic")
async def get_statistic(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.answer(text="Выберите период", reply_markup=choose_period_keyboard())
        await state.set_state(AdminStates.get_period)
        await callback.answer()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")


@router_get_statistic.message(AdminStates.get_period)
async def show_statistic(message: Message, state: FSMContext):
    try:
        message_text = message.text.lower()
        if message_text == "назад":
            await message.answer(
                text="Период не выбран",
                reply_markup=clear_keyboard()
            )
            await message.answer_photo(
                photo=FSInputFile("app/images/brand/logo.png"),
                caption="Панель админа",
                reply_markup=admin_panel()
            )
            await state.clear()
        elif message_text in ["сегодня", "вчера", "неделя", "месяц", "3 месяца", "6 месяцев"]:
            is_created_statistic = visualization_analytics(period=message_text)
            if is_created_statistic:
                await message.answer(
                    text=f"Данные за период ({message_text})",
                    reply_markup=clear_keyboard()
                )
                await message.answer_photo(
                    photo=FSInputFile("app/images/tmp/statistic.png"),
                    caption="График для аналитики",
                    reply_markup=admin_panel()
                )
                delete_tmp_image()
                await state.clear()
            else:
                await message.answer(text="Запрос не был корректно обработан, попробуйте еще раз")
        else:
            await message.delete()
    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
