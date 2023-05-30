from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import r_p_s_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner, check_user, get_score

# инициализируем роутер
router: Router = Router()


# хэндлер для /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'].format(
        message.from_user.full_name), reply_markup=yes_no_kb)
    check_user(message.from_user.id)


# хэндлер для /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# хэндлер, срабатывающий на согласие сыграть
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=r_p_s_kb)


# хэндлер, срабатывающий на отказ играть
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_button(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# хэндлер, срабатывающий на игровые кнопки
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice, message.from_user.id)
    await message.answer(text=LEXICON_RU[winner].format(
        get_score(message.from_user.id)), reply_markup=yes_no_kb)
