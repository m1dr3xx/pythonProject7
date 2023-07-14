from aiogram.fsm.state import StatesGroup, State


class MagicBallState(StatesGroup):
    is_running = State()

class RPSState(StatesGroup):
    is_running = State()

class NumbersState(StatesGroup):
    is_running = State()