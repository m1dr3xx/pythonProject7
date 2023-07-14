from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

rock = KeyboardButton(text='Камень 🪨')
paper = KeyboardButton(text='Бумага 📃')
scissors = KeyboardButton(text='Ножницы ✂️')

rsp_keyboard = ReplyKeyboardMarkup(keyboard=[
    [rock, paper, scissors]
], resize_keyboard=True)