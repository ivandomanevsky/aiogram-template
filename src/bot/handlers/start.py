from aiogram import Router, types
from aiogram.filters import CommandStart
from src.bot.filtres.is_admin import IsAdmin
from src.bot.keyboards.user import menu_keyboard

router = Router()


@router.message(CommandStart(), IsAdmin())
async def start_for_admin(message: types.Message):
    await message.answer('Start message for admin')


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Start message', reply_markup=menu_keyboard)
