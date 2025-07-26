from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    change_info = State()
    get_filename = State()
    get_file = State()
    get_period = State()
