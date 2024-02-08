from aiogram import Router, filters, types

from markups.weather import find_weather_kb

router = Router()


@router.message(filters.CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello! I'm a bot!", reply_markup=find_weather_kb)
