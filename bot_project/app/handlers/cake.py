from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from data_from_database import get_levels, get_form, get_toppings

levels = get_levels()
forms = get_form()
toppings = get_toppings()


class OrderCake(StatesGroup):
    waiting_for_levels = State()
    waiting_for_form = State()
    waiting_for_toppings = State()


async def level_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in levels:
        keyboard.add(name)
    await message.answer("Выберите сколько уровней в торте:", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_levels.state)


async def level_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in levels:
        await message.answer("Пожалуйста, выберите уровень торта, используя клавиатуру ниже.")
        return
    await state.update_data(cake_level=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in forms:
        keyboard.add(size)
    await state.set_state(OrderCake.waiting_for_form.state)
    await message.answer("Теперь выберите форму торта:", reply_markup=keyboard)


async def form_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in forms:
        await message.answer("Пожалуйста, выберите форму торта, используя клавиатуру ниже.")
        return
    await state.update_data(cake_form=message.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in forms:
        keyboard.add(size)
    # user_data = await state.get_data()
    await state.set_state(OrderCake.waiting_for_toppings.state)
    await message.answer("Теперь выберите топпинг торта:", reply_markup=keyboard)


async def topping_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in toppings:
        await message.answer("Пожалуйста, выберите топпинг, используя клавиатуру ниже.")
        return
    await state.update_data(cake_topping=message.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for topping in toppings:
        keyboard.add(topping)
    await message.answer("Теперь выберите еще что-то торта:", reply_markup=keyboard)
    user_data = await state.get_data()
    # await state.set_state(OrderCake.waiting_for_toppings.state)
    # await message.answer("Теперь выберите топпинг торта:", reply_markup=keyboard)
    # user_data = await state.get_data()
    await message.answer(f"Вы заказали:\n {user_data['cake_level']}\n {user_data['cake_form']} \n {user_data['cake_topping']}\n Итого:  ", reply_markup=types.ReplyKeyboardRemove())
    # await state.finish()
    # user_data = await state.get_data()
    # await message.answer(f"Вы заказали {message.text.lower()} порцию {user_data['chosen_food']}.\n"
    #                      f"Попробуйте теперь заказать напитки: /drinks", reply_markup=types.ReplyKeyboardRemove())
    # await state.finish()


def register_handlers_cake(dp: Dispatcher):
    dp.register_message_handler(level_start, commands="cake", state="*")
    dp.register_message_handler(level_chosen, state=OrderCake.waiting_for_levels)
    dp.register_message_handler(form_chosen, state=OrderCake.waiting_for_form)
    dp.register_message_handler(topping_chosen, state=OrderCake.waiting_for_toppings)
