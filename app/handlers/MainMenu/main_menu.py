from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from ..basic.basic_keyboard import gvaText

"""
    INSTRUCTION

    REGISTER
    |   
    |___startRegistering (func)

"""


class MainMenuState(StatesGroup):
    detect = State()


async def detectOption(poMessage: types.Message, poState: FSMContext = None):
    vsText = poMessage.text
    if vsText not in gvaText:
        await poMessage.answer('Please Choose from Options Below 😄')
    else:
        if vsText == gvaText[0]:
            # TODO Start Broning
            await poMessage.answer('You are Broning')
            return
        elif vsText == gvaText[1]:
            # TODO Your Barber
            await poMessage.answer('there is no barber of yours')
            return
        elif vsText == gvaText[2]:
            # TODO For Future
            await poMessage.answer(vsText)
            return
        elif vsText == gvaText[3]:
            # TODO Settings
            await poMessage.answer(vsText)
            return


def registerHandlerMainMenu(poDp: Dispatcher):
    poDp.register_message_handler(detectOption, state=MainMenuState.detect)
