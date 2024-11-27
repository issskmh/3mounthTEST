from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="send home work",
                    callback_data="home_work"
                )
            ]
        ]
    )
    await message.answer('Hello, ' + name, reply_markup=kb)
