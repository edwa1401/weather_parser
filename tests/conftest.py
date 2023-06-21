import pytest
from fast_api_client.model import Weather
from fast_api_client.config import Config
import requests
import io
import json


@pytest.fixture
def make_api_key():
    config = Config(
        api_key='12345'
        )
    return config

@pytest.fixture
def convert_dict_to_bytes():
    def inner(temp: float | None = None, temp_feels_like: float | None = None, weather_description: str | None = None, humidity: int | None = None):
        weather = {
            "coord":
            {
                "lon":37.6156,
                "lat":55.7522
            },
            "weather":
            [
                {
                    "id":802,
                    "main":"Clouds",
                    "description":weather_description or "Солнечно",
                    "icon":"03d"
                }
            ],
            "base":"stations",
            "main":
            {
                "temp":temp or 25.00,
                "feels_like":temp_feels_like or 30.00,
                "temp_min":25.1,
                "temp_max":26.29,
                "pressure":1012,
                "humidity":humidity or 80,
                "sea_level":1012,
                "grnd_level":995
            },
            "visibility":10000,
            "wind":
            {
                "speed":3.54,
                "deg":36,
                "gust":7.66
            },
            "clouds":
            {
                "all":44
            },
            "dt":1686933677,
            "sys":
            {
                "type":1,
                "id":9027,
                "country":"RU",
                "sunrise":1686876269,
                "sunset":1686939352
            },
            "timezone":10800,
            "id":524901,
            "name":"Урюпинск",
            "cod":200
        }
        content = json.dumps(weather).encode()
        return content
    return inner


@pytest.fixture
def make_request_response(convert_dict_to_bytes):
    response = requests.Response()
    response.status_code = 200
    response.raw = io.BytesIO(convert_dict_to_bytes())
    return response


@pytest.fixture
def make_openweather_data():
    def inner(temp: float | None = None, temp_feels_like: float | None = None, weather_description: str | None = None, humidity: int | None = None):
        weather = {
            "coord":
            {
                "lon":37.6156,
                "lat":55.7522
            },
            "weather":
            [
                {
                    "id":802,
                    "main":"Clouds",
                    "description":weather_description or "Солнечно",
                    "icon":"03d"
                }
            ],
            "base":"stations",
            "main":
            {
                "temp":temp or 25.00,
                "feels_like":temp_feels_like or 30.00,
                "temp_min":25.1,
                "temp_max":26.29,
                "pressure":1012,
                "humidity":humidity or 80,
                "sea_level":1012,
                "grnd_level":995
            },
            "visibility":10000,
            "wind":
            {
                "speed":3.54,
                "deg":36,
                "gust":7.66
            },
            "clouds":
            {
                "all":44
            },
            "dt":1686933677,
            "sys":
            {
                "type":1,
                "id":9027,
                "country":"RU",
                "sunrise":1686876269,
                "sunset":1686939352
            },
            "timezone":10800,
            "id":524901,
            "name":"Урюпинск",
            "cod":200
        }
        return weather
    return inner


@pytest.fixture
def make_weather():
    def inner(temp: float | None = None, temp_feels_like: float | None = None, weather_description: str | None = None, humidity: int | None = None):
        return Weather(
            temp=temp or 25.00,
            temp_feels_like=temp_feels_like or 30.00,
            weather_description=weather_description or "Солнечно",
            humidity=humidity or 80,
        )
    return inner


