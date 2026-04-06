import httpx
import asyncio
import logging
from typing import List

logger = logging.getLogger("weather_api")

class WeatherAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.weather.com/city/{}", max_concurrent: int = 5):
        self.api_key = api_key
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.client = httpx.AsyncClient(timeout=10)  

    async def fetch_city(self, city: str) -> dict:
        """
        Fetch weather for a single city with error handling.
        """
        async with self.semaphore:
            try:
                response = await self.client.get(
                    self.base_url.format(city),
                    params={"apikey": self.api_key}
                )
                response.raise_for_status()
                return {city: response.json()}
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error for {city}: {e.response.status_code}")
                return {city: f"HTTP error {e.response.status_code}"}
            except httpx.RequestError as e:
                logger.error(f"Request error for {city}: {str(e)}")
                return {city: f"Request error: {str(e)}"}

    async def fetch_multiple(self, cities: List[str]) -> dict:
        """
        Fetch weather for multiple cities concurrently.
        """
        tasks = [self.fetch_city(city) for city in cities]
        results = await asyncio.gather(*tasks)
        return {k: v for d in results for k, v in d.items()}

    async def close(self):
        """
        Close the HTTP client when app shuts down.
        """
        await self.client.aclose()