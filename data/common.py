from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.vibor import vibor_keyboard

start=Router()

@start.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет! Я бот который умеет играть в целых три игры! Выбери игру в которую будем играть: ", reply_markup=vibor_keyboard)
