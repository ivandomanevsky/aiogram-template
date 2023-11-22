from aiogram import F, Router, types

from src.bot.keyboards.user import button_3_inline_keyboard

router = Router()


@router.message(F.text == 'Button 1')
async def click_on_button_1(message: types.Message):
    await message.answer('Clicked on button 1', reply_markup=button_3_inline_keyboard())
