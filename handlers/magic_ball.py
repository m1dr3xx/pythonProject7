from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from AI.answers import answers
from callbacks.for_game import GameCallbackData
from states.games import MagicBallState

mag = Router()

@mag.callback_query(
    GameCallbackData.filter(F.game == 'magic_ball')
)
async def start_command(query: CallbackQuery, state: FSMContext):
    await query.message.answer("Привет! Я твой бот магический шар.  ")
    await query.answer()
    await state.set_state(MagicBallState.is_running)

@mag.message(StateFilter(MagicBallState.is_running))
async def help_command(message: Message):
    await message.answer("Можешь задавать мне вопросы о жизни я буду отвечать.")


@mag.message(F.text)
async def do_answer(message: Message):
    answer = answers.generate_answer()
    if answer:
        await message.answer(answer)