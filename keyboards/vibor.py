from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.for_game import GameCallbackData

rps = InlineKeyboardButton(
    text='Камень, Ножницы, Бумага',
    callback_data=GameCallbackData(game="rps").pack()
)
magic_ball = InlineKeyboardButton(
    text='Магический шар',
    callback_data=GameCallbackData(game="magic_ball").pack()
)

numbers = InlineKeyboardButton(
    text='Угадай число',
    callback_data=GameCallbackData(game="numbers").pack()
)

vibor_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [rps],
    [magic_ball],
    [numbers]
])
