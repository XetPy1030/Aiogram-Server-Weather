from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import StatesGroup, State

find_weather_text = "Узнать погоду"
cancel_text = "Отмена"

find_weather_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True, keyboard=[
        [
            types.KeyboardButton(text=find_weather_text)
        ]
    ]
)

cancel_kb = types.ReplyKeyboardMarkup(
    resize_keyboard=True, keyboard=[
        [
            types.KeyboardButton(text=cancel_text)
        ]
    ]
)


class WeatherState(StatesGroup):
    city = State()
