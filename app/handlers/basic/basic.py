# Standard Library

# Aiogram Stuff
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import IDFilter, Text
from aiogram.dispatcher.filters.state import State, StatesGroup

# First Partly Stuff
from .basic_keyboard import close, StartMenuKeyboard


# State Groups
from ..register.reg import startRegistering
from ..MainMenu.main_menu import detectOption

"""
    INSTRUCTION
    
    BASIC
    |   
    |___ start (func)
    |   |
    |   | Checks if there any state if it's, finishes it and Opens start menu
    |   | Checks if User is already registered, If True then Opens start menu
    |   | If User Is not registered then Starts Register Handlers
    |
    |___ cancel (func)
    |   |
    |   |-Finishes any state
    |
    |___ registerHandlerBasic (func)
        |
        |-registers funcs to Dispatcher
"""

fake_db = []
# 431510980


# Start Command
async def start(poMessage: types.Message, poState: FSMContext = None):
    # Ends any state which was started before
    if poState is not None:
        await poState.finish()
        await poMessage.answer('Do you wanna Bron', reply_markup=StartMenuKeyboard)

    if poMessage.chat.id in fake_db:
        # TODO for registered users
        await poMessage.answer('Do you wanna Bron', reply_markup=StartMenuKeyboard)

    else:
        # TODO start register state
        await startRegistering(poMessage, poState)


# Cancel Command
async def cancel(poMessage: types.Message, poState: FSMContext = None):
    # Ends any state which was started before
    if poState is not None:
        await poState.finish()
        await poMessage.answer('Canceled', reply_markup=close)

    await poMessage.answer('Canceled')


# Register Handler
def registerHandlerBasic(poDp: Dispatcher):
    poDp.register_message_handler(start, commands='start', state='*')
    poDp.register_message_handler(cancel, commands='cancel', state='*')
