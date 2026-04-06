from fastapi import FastAPI
from weather_api import WeatherAPI

app = FastAPI()


weather_api = WeatherAPI(api_key="FastApi")  

@app.get("/weather")
async def get_weather(cities: list[str]):
    """
    Endpoint to fetch weather for multiple cities concurrently.
    Example: /weather?cities=London&cities=Paris&cities=Tokyo
    """
    data = await weather_api.fetch_multiple(cities)
    return data

@app.on_event("shutdown")
async def shutdown_event():
    await weather_api.close()