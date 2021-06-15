from aiogram.types.reply_keyboard import (KeyboardButton, ReplyKeyboardMarkup,
                                          ReplyKeyboardRemove)

close = ReplyKeyboardRemove()

gvaText = ['🤙Bron Time', '💇‍♂️Your Barber', '📺', '⚙️Settings']

StartMenuKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=gvaText[0])],
        [KeyboardButton(text=gvaText[1]), KeyboardButton(text=gvaText[2])],
        [KeyboardButton(text=gvaText[3])]
    ],
    resize_keyboard=True
)




