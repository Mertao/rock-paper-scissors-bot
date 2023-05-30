import random

from lexicon.lexicon_ru import LEXICON_RU


# список пользователей
users: dict = {}


# проверяем, есть ли пользователь в списке и добавляем если нет
def check_user(user_id: str) -> None:
    if user_id not in users:
        users[user_id] = {'user_score': 0,
                          'bot_score': 0}


# возвращаем счет в виде строки
def get_score(user_id: str) -> str:
    return f"{users[user_id]['bot_score']} : {users[user_id]['user_score']}"


# генерируем ответ бота
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# получаем ключ по ответу пользователя из словаря для дальнейшей работы
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


# определяем победителя
def get_winner(user_choice: str, bot_choice: str, user_id: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}

    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        users[user_id]['user_score'] += 1
        return 'user_won'
    else:
        users[user_id]['bot_score'] += 1
        return 'bot_won'
