import uvicorn
from fastapi import FastAPI

from fast_api_client.config import load
from fast_api_client.weather import get_weather_by_city

app = FastAPI()


@app.get("/weather")
def get_weather(city: str) -> dict | str:
    config = load()
    weather = get_weather_by_city(city=city, config=config)
    if weather:
        return {
            "температура": weather.temp,
            "температура, ощущается как": weather.temp_feels_like,
            "погода": weather.weather_description,
            "влажность": weather.humidity
            }
    else:
        return 'сайт openweathermap.org сейчас недоступен'


if __name__ == "__main__":
    uvicorn.run(app)
