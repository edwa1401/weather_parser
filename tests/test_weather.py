from unittest.mock import patch

import pytest

from fast_api_client.weather import convert, get_weather_by_city


def test__convert__success(make_openweather_data, make_weather):
    assert convert(make_openweather_data()) == make_weather()


@pytest.mark.xfail(reason='difference in input data from expected results')
def test__convert__fail(make_openweather_data, make_weather):
    assert convert(make_openweather_data(temp=20)) == make_weather(weather_description="Туманно")


def test__get_weather_by_city__success(make_request_response, make_weather, make_api_key):
    weather = make_weather()
    config = make_api_key
    with patch('fast_api_client.weather.requests.get') as request_get_mock:
        request_get_mock.return_value = make_request_response
        assert get_weather_by_city("Moscow", config) == weather


@pytest.mark.xfail(reason='differences in input and return')
def test__get_weather_by_city__fail(make_request_response, make_weather, make_api_key):
    weather = make_weather()
    config = make_api_key
    with patch('fast_api_client.weather.requests.get') as request_get_mock:
        request_get_mock.return_value = make_request_response(humidity=100)
        assert get_weather_by_city("Moscow", config) == weather

# TODO add test to request exeptions