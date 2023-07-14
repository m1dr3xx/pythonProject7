from random import choice

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from callbacks.for_game import GameCallbackData
from states.games import RPSState

sps = Router()
@sps.callback_query(
    GameCallbackData.filter(F.game == 'rps'))   # Берём только сообщения, являющиеся командой /start
async def start_command(query: CallbackQuery, state: FSMContext):  # message - сообщение, которое прошло через фильтр
    await query.message.answer("Привет! Сыграем в камень, ножницы, бумага!!!!",)
    await query.answer()
    await state.set_state(RPSState.is_running)


@sps.message(StateFilter(RPSState.is_running))
async def handle_rps_game(message: Message):
    variants = ('Камень 🪨', 'Бумага 📃', 'Ножницы ✂️')
    user_choice = message.text
    if user_choice in variants:
        bots_choice = choice(variants)
        await message.answer(f'Я выбрал {bots_choice}')
        if (bots_choice == 'Бумага 📃' and user_choice == 'Камень 🪨' or
                bots_choice == 'Ножницы ✂️' and user_choice == 'Бумага 📃' or
                bots_choice == 'Камень 🪨' and user_choice == 'Ножницы ✂️'
        ):
            await message.answer('Я победил 😈')
        elif bots_choice == user_choice:
            await message.answer('Ничья 🤕')
        else:
            await message.answer('Я проиграл 😢')
    else:
        await message.answer('Вы написали кринж')