import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("CLIMATE_KEY")
if not key:
    raise ValueError("API key not found.")

city = input("Enter the city for view climate: ")

def fetch_data(city, filters={}):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=pt_br"
    response = requests.get(url, params=filters)
    if response.status_code == 200:
        return response.json()
    else:
        return None

data = fetch_data(city, filters={})
if data:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind:", data["wind"]["speed"], "m/s")
    print("Climate:", data["weather"][0]["description"])
else:
    print("Error: not disponible datas.")