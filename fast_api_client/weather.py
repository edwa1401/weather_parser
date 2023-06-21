import requests
from requests.exceptions import RequestException

from fast_api_client.config import Config
from fast_api_client.model import Weather


def get_weather_by_city(city: str, config: Config) -> Weather:

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": config.api_key,
        "units": 'metric',
        "lang": 'ru'
    }

    try:
        result = requests.get(url, params=params)
    except RequestException as error:
        print(str(error))
    data = result.json()
    return convert(data)


def convert(weather: dict) -> Weather:
    return Weather(
        temp=weather['main']['temp'],
        temp_feels_like=weather['main']['feels_like'],
        weather_description=weather['weather'][0]['description'],
        humidity=weather['main']['humidity'],
    )
