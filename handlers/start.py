from aiogram import Router, filters, types
from aiogram.fsm.context import FSMContext

from markups.weather import find_weather_kb

router = Router()


@router.message(filters.CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Hello! I'm a bot!", reply_markup=find_weather_kb)
    await state.clear()
