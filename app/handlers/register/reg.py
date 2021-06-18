from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .reg_keyboard import StartKeyboard, close
from ..basic.basic_keyboard import StartMenuKeyboard
from ..MainMenu.main_menu import detectOption, MainMenuState

"""
    INSTRUCTION

    REGISTER
    |   
    |___startRegistering (func)
    |   |
    |   | Opens RegisterStartKeyboard
    |   |
     
"""


# TODO Add Choosing Barber

class RegisterUserState(StatesGroup):
    getContact = State()


async def getContactInfo(poMessage: types.Message, poState: FSMContext = None):
    if poMessage.contact is not None:
        # TODO Register Contact
        await poMessage.answer('Do you wanna Bron', reply_markup=StartMenuKeyboard)
        await MainMenuState.detect.set()
        # await detectOption(poMessage, poState)
    else:
        await poMessage.answer('Please Register Before', reply_markup=StartKeyboard)
        return


def registerHandlerRegister(poDp: Dispatcher):
    poDp.register_message_handler(getContactInfo, state=RegisterUserState.getContact, content_types=['contact', 'text'])
