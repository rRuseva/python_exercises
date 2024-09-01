from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city: str = 'Ruse') -> dict:
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n *** Get current weather conditions ***\n')

    city = input("\nPlease enter city name: ")
    # Validate that the input is not empty string or only spaces
    if not bool(city.strip()):
        city = "Ruse"

    weather_data = get_current_weather(city=city)

    print()
    # print(type(weather_data))
    pprint(weather_data)