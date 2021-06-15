from aiogram.types.reply_keyboard import (KeyboardButton, ReplyKeyboardMarkup,
                                          ReplyKeyboardRemove)

close = ReplyKeyboardRemove()

StartKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👤Give Contact Info', request_contact=True)],
        [KeyboardButton(text='↪️Back')]
    ],
    resize_keyboard=True
)
