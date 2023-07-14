import random

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from callbacks.for_game import GameCallbackData
from states.games import NumbersState

num = Router()


@num.callback_query(
    GameCallbackData.filter(F.game == 'numbers')
)  # Берём только сообщения, являющиеся командой /start
async def start_command(query: CallbackQuery, state: FSMContext):  # message - сообщение, которое прошло через фильтр
    await query.message.answer(
        "Привет, сыграем в игру - я загадал число от 1 до 3, а ты угадывай\n")  # Отвечаем на полученное сообщение
    await query.answer()
    await state.set_state(NumbersState.is_running)


@num.message(StateFilter(NumbersState.is_running))
async def handle_number(message: Message):
    if message.text.isdigit():
        number = random.randint(1, 3)  # генерируем число только после ответа пользователя, а не до.
        if number == int(message.text):
            await message.answer('Да! Вы угадали. Я перезагадал число')
        else:
            await message.answer('Нет! Вы не угадали((( Я перезагадал число')
