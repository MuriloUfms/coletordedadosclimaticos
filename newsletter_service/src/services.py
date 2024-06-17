import requests
from settings import Settings


def get_data():
    response = requests.post(
        f'{Settings.API_COLECTOR_URL}/collect',
        json={'latitude': -20.5026554, 'longitude': -54.6154765},
    )
    response.raise_for_status()
    return response.json()
