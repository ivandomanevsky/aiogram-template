from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_1 = KeyboardButton(text='Button 1')
button_2 = KeyboardButton(text='Button 2')

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True)


def button_3_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='Button 3', callback_data='Button 3')
    builder.adjust(1)
    return builder.as_markup()
