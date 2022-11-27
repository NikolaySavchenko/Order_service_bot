import logging
from aiogram import Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from environs import Env

from core import get_levels, get_form


telegram_token = '5945463620:AAGnF8c_DSNkx60EzEqI2riWeqVMA0gecDg'

bot = Bot(telegram_token, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

levels = get_levels()
forms = get_form()


class OrderCake(StatesGroup):
    choose_level = State()
    choose_form = State()
    choose_topping = State()


@dp.message_handler(commands='start')
async def test(message: types.Message):
    await message.reply('Test')


@dp.message_handler(commands='cake')
async def cake_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in levels:
        keyboard.add(name)
    await message.answer('Выберете сколько будет уровней у торта:', reply_markup=keyboard)
    await state.set_state(OrderCake.choose_level.state)


async def choose_form(message: types.Message, state: FSMContext):
    if message.text.lower() not in levels:
        await message.answer("Пожалуйста, выберите уровень торта.")
        return
    await state.update_data(chosen_level=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for form in forms:
        keyboard.add(form)
    await state.set_state(OrderCake.choose_form.state)
    await message.answer('Теперь выберите форму торта:', reply_markup=keyboard)


async def choose_topping(message: types.Message, state: FSMContext):
    if message.text.lower() not in forms:
        await message.answer("Пожалуйста, выберите топпинг, используя клавиатуру ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы заказали {message.text.lower()} порцию {user_data['chosen_level']}.\n"
                         f"Попробуйте теперь заказать напитки: /drinks", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(cake_start, commands="cake", state="*")
    dp.register_message_handler(choose_form, state=OrderCake.choose_level)
    dp.register_message_handler(choose_topping, state=OrderCake.choose_topping)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
