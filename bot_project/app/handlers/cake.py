from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from data_from_database import get_levels, get_form, get_toppings, get_berry, get_decor

levels = get_levels()
forms = get_form()
toppings = get_toppings()
berries = get_berry()
decors = get_decor()


class OrderCake(StatesGroup):
    waiting_for_levels = State()
    waiting_for_forms = State()
    waiting_for_toppings = State()
    waiting_for_berry = State()
    waiting_for_decor = State()
    waiting_for_ready = State()


async def level_start(message: types.Message, state: FSMContext, ):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for level in levels:
        keyboard.add(level)
    await message.answer("Выберите количество уровней торта:", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_forms.state)



async def form_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in forms:
        await message.answer("Пожалуйста, выберите форму торта, используя клавиатуру ниже.")
        return
    await state.update_data(cake_level=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in forms:
        keyboard.add(size)
    await message.answer("Теперь выберите форму торта:", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_toppings.state)


async def topping_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in toppings:
        await message.answer("Пожалуйста, выберите топпинг, используя клавиатуру ниже.")
        return
    await state.update_data(cake_form=message.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for topping in toppings:
        keyboard.add(topping)
    await message.answer("выберите топпинг", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_berry.state)


async def berry_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in toppings:
        await message.answer("Пожалуйста, выберите топпинг, используя клавиатуру ниже.")
        return
    await state.update_data(cake_topping=message.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for berry in berries:
        keyboard.add(berry)
    await message.answer("Добавьте ягод:", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_decor.state)


async def decor_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() in toppings:
        await message.answer("Пожалуйста, выберите декор, используя клавиатуру ниже.")
        return
    await state.update_data(cake_berry=message.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for decor in decors:
        keyboard.add(decor)
    await message.answer("Добавьте декор:", reply_markup=keyboard)
    await state.set_state(OrderCake.waiting_for_ready.state)


async def cake_is_ready(message: types.Message, state: FSMContext):
    await state.update_data(cake_decor=message.text.lower())
    user_data = await state.get_data()
    await message.answer(text=f"Вы заказали: \n{user_data['cake_level']} \n{user_data['cake_form']}\n"
                              f"{user_data['cake_topping']}\n{user_data['cake_berry']}\n{user_data['cake_decor']}",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_cake(dp: Dispatcher):
    dp.register_message_handler(level_start, commands="cake", state="*")

    dp.register_message_handler(form_chosen, state=OrderCake.waiting_for_forms)
    dp.register_message_handler(topping_chosen, state=OrderCake.waiting_for_toppings)
    dp.register_message_handler(berry_chosen, state=OrderCake.waiting_for_berry)
    dp.register_message_handler(decor_chosen, state=OrderCake.waiting_for_decor)
    dp.register_message_handler(cake_is_ready, state=OrderCake.waiting_for_ready)


