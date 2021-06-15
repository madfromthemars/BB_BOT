# Standard library
import asyncio
import logging

# Aiogram Stuff
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

# First partly stuff
from app.config_reader import load_config

# Handlers:
from app.handlers.basic.basic import registerHandlerBasic
from app.handlers.register.reg import registerHandlerRegister
from app.handlers.MainMenu.main_menu import registerHandlerMainMenu

gLogger = logging.getLogger(__name__)


# Registers Commands
async def setCommands(poBot: Bot):
    vaoCommands = [
        BotCommand(command='/start', description="Start Bot"),
        BotCommand(command='/cancel', description="Cancel")
    ]

    await poBot.set_my_commands(vaoCommands)


async def main():
    # logging.basicConfig(
    #     # level=logging.INFO,
    #     format='%(asctime)s - %(levelname)s - %(names)s - %(messages)s',
    # )
    # gLogger.error('Starting bot')
    print('Bot Started')

    voConfig = load_config('config/bot.ini')

    voBot = Bot(token=voConfig.tg_bot.token)
    voDp = Dispatcher(voBot, storage=MemoryStorage())

    # Registering Handlers
    registerHandlerBasic(voDp)
    registerHandlerRegister(voDp)
    registerHandlerMainMenu(voDp)

    await setCommands(voBot)
    await voDp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
