from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ------- создаем клавиатуру с ответами -------
# создаем кнопкис ответами да/нет
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# инициализируем билдер для клавиатуры с кнопками давай/не хочу
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# добавляем кнопки в билдер
yes_no_kb_builder.row(button_yes, button_no, width=2)

# создаем клавиатуру с кнопками дивай/не хочу
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)


# ------- создаем игровую клавиатуру -------
# создаем кнопки с камнем/ножницами/бумагой
rock_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
paper_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
scissors_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])

# инициализируем билдер для игровой клавиатуры
r_p_s_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# добавляем кнопки в билдер
r_p_s_builder.row(rock_button, paper_button, scissors_button, width=1)

# создаем игровую клавиатуру
r_p_s_kb = r_p_s_builder.as_markup(resize_keyboard=True)
