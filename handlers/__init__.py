from core import dp

from .start import router as start_router
from .weather import router as weather_router

dp.include_routers(start_router, weather_router)
