from pydantic import BaseModel


class Weather(BaseModel):
    temp: float
    temp_feels_like: float
    weather_description: str
    humidity: int
