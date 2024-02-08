from aiogram import Router, F, types, filters
from aiogram.fsm.context import FSMContext

from config import WEATHER_FORMAT
from markups.weather import find_weather_text, WeatherState, cancel_kb, find_weather_kb
from utils.weather import get_weather

router = Router()


@router.message(filters.Command("weather"))
async def weather(message: types.Message, state: FSMContext):
    await setup_weather(message, state)


async def setup_weather(message, state):
    await message.answer("Введите город", reply_markup=cancel_kb)
    await state.set_state(WeatherState.city)


@router.message(F.text == find_weather_text)
async def find_weather(message: types.Message, state: FSMContext):
    await setup_weather(message, state)


@router.message(F.text == "Отмена")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено", reply_markup=find_weather_kb)
    await state.clear()


@router.message(filters.StateFilter(WeatherState.city))
async def get_weather_handler(message: types.Message, state: FSMContext):
    city = message.text or message.caption
    weather = get_weather(city)
    if not weather:
        await message.answer("Город не найден или произошла ошибка", reply_markup=find_weather_kb)
        await state.clear()
        return

    kwargs = {
        **weather,
        "city": city
    }
    await message.answer(WEATHER_FORMAT.format(**kwargs), reply_markup=find_weather_kb)

    await state.clear()
