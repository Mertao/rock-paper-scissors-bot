import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


# инициализируем логгер
logger = logging.getLogger(__name__)


# конфигурирование и запуск бота
async def main():
    # конфигурируем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # выводим в консоль информацию о запуске бота
    logger.info('Starting bot')

    # загружаем конфиг в переменную config
    config: Config = load_config()

    # инициализируем бота и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # регистрируем роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    # запускаем пулинг
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
