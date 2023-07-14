from random import choice

answers = [

    'Конечно',
    'Думаю, да',
    'Возможно',
    'Нет',
    'Вряд ли'


]


def generate_answer():
    return choice(answers)