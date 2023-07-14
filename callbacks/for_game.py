from aiogram.filters.callback_data import CallbackData


class GameCallbackData(CallbackData, prefix='game'):
    game: str
