# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

import os
from dotenv import load_dotenv
import requests

load_dotenv()
api = os.getenv('API_KEY')

def get_temp(api, cidade):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}'
    resposta = requests.get(url).json()
    print(resposta)

get_temp(api,'Maputo')

