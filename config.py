from decouple import config

TOKEN = config('TOKEN')
SERVER_URL = config('SERVER_URL')

WEATHER_FORMAT = """
Город: {city}
Температура: {temperature}°C
Давление: {pressure} мм.рт.ст.
Скорость ветра: {wind_speed} м/с
"""
