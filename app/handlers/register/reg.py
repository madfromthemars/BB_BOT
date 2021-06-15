from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .reg_keyboard import StartKeyboard, close
from ..basic.basic_keyboard import StartMenuKeyboard
from ..MainMenu.main_menu import detectOption

"""
    INSTRUCTION

    REGISTER
    |   
    |___startRegistering (func)
    |   |
    |   | Opens RegisterStartKeyboard
    |   |
     
"""


class RegisterUserState(StatesGroup):
    start = State()
    getContact = State()


# Initialize Registration
async def startRegistering(poMessage: types.Message, poState: FSMContext):
    await poMessage.answer('Firstly I need your Contact Info', reply_markup=StartKeyboard)
    await State.set(RegisterUserState.getContact)


async def getContactInfo(poMessage: types.Message, poState: FSMContext):
    voContact = poMessage.contact
    print(poMessage)

    if poMessage.contact is not None:
        # TODO Register Contact
        await poMessage.answer('Do you wanna Bron', reply_markup=StartMenuKeyboard)
        await detectOption(poMessage, poState)
    else:
        await poMessage.answer('Please Register Before', reply_markup=StartKeyboard)
        return


def registerHandlerRegister(poDp: Dispatcher):
    poDp.register_message_handler(startRegistering, state=RegisterUserState.start)
    poDp.register_message_handler(getContactInfo, state=RegisterUserState.getContact)
