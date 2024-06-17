import requests
from fastapi import HTTPException, status

from settings import Settings


def coletar_dados_climaticos(latitude: float, longitude: float):
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': Settings.OPEN_WEATHER_API_KEY,
        'units': 'metric',
    }
    response = requests.get(Settings.OPEN_WEATHER_URL, params=params)

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao acessar API do OpenWeather: "
            f'cod={response.status_code}, message={response.json()["message"]}',
        )

    data = response.json()
    return {
        'temperatura': data['main']['temp'],
        'umidade': data['main']['humidity'],
        'velocidade_vento': data['wind']['speed'],
        'direcao_vento': data['wind']['deg'],
    }
