import requests

from config import SERVER_URL


def get_weather(city: str) -> dict | None:
    url = f'{SERVER_URL}/weather'
    params = {
        'city': city
    }
    response = requests.get(url, params=params)
    if not response.ok:
        return None

    return response.json()
