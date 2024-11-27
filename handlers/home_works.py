from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot_config import database


hw_router = Router()

class HomeWork(StatesGroup):
    name = State()
    python_group = State()
    hw_number = State()
    git_url = State()

@hw_router.callback_query(F.data == "home_work")
async def start_home_work(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("введите ваше имя:")
    await state.set_state(HomeWork.name)
    await callback_query.answer()


@hw_router.message(HomeWork.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Python-47_1"),
                KeyboardButton(text="Python-48_1")
            ],
            [
                KeyboardButton(text="Python-47_2"),
                KeyboardButton(text="Python-48_2")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="ваша группа"
    )
    await message.answer("выберите с какой вы группы", reply_markup=kb)
    await state.set_state(HomeWork.python_group)


@hw_router.message(HomeWork.python_group)
async def group(message: Message, state: FSMContext):
    await state.update_data(python_group=message.text)
    await message.answer("введите номер домашнего задания (от 1 до 8)", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(HomeWork.hw_number)


@hw_router.message(HomeWork.hw_number)
async def hw_number(message: Message, state: FSMContext):
    if message.text.isdigit():
        number = int(message.text)
        if 1 <= number <= 8:
            await state.update_data(hw_number=number)
            await message.answer("введите ссылку на GIT репозиторий")
            await state.set_state(HomeWork.git_url)
        else:
            await message.answer("введите число от 1 до 8")
    else:
        await message.answer("введите число")


@hw_router.message(HomeWork.git_url)
async def check(message: Message, state: FSMContext):
    await state.update_data(git_url=message.text)
    github_url = message.text
    if github_url.startswith("https://github.com"):
        await message.answer("ваше дз было сохранено!")
        data = await state.get_data()
        database.execute(
            query="""
                INSERT INTO homeworks (name, python_group, homework_number, git_url)
                VALUES (?, ?, ?, ?)
                """,
            params=(data["name"], data["python_group"], data["hw_number"], data["git_url"])
        )
        await state.clear()
    else:
        await message.answer("ссылка должна начинаться с - https://github.com")