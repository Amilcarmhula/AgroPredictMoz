from datetime import datetime, timedelta, timezone

sunrise = 1744862757
sunset = 1744903922

sunrise_utc = datetime.fromtimestamp(sunrise,timezone.utc)
sunset_utc = datetime.fromtimestamp(sunset, timezone.utc)

sunrise_local = sunrise_utc+timedelta(hours=2)
sunset_local = sunset_utc+timedelta(hours=2)

print('nascer do sol:',sunrise_local.strftime('%H:%M:%S'))
print('por do sol:',sunset_local.strftime('%H:%M:%S'))
duracao = sunset_local - sunrise_local
duracao = duracao.total_seconds()/3600
print(f'Duracao do sol: {round(duracao,2)}')
print(f'Duracao do sol: {round(duracao)}')


coordenadas = {
    'Maputo(Provincia)':(-25.9622,32.4600),
    'Maputo(Cidade)': (-25.9653,32.5892),
    'Gaza': (-25.0519,33.6442),
    'Inhambane': (-23.8650,35.3833),
    'Manica': (-19.1164,33.4830),
    'Sofala': (-19.8333,34.8500),
    'Tete': (-16.1564,33.5867),
    'Zambezia': (-17.8786,36.8883),
    'Nampula': (-15.1165,39.2666),
    'Niassa': (-13.3120,35.2406),
    'Cabo Delgado': (-12.9675,40.5528)
}



import os
from dotenv import load_dotenv
import requests
from typing import List
from datetime import  datetime

load_dotenv()
api = os.getenv('API_KEY')

def get_temp(api, cidade):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}'
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat=-25.9653&lon=32.5892&appid={api}'
    # url = f'https://api.openweathermap.org/data/2.5/weather?lat=-15.1165&lon=39.2666&&appid={api}'
    resposta = requests.get(url).json()
    print(resposta)
    print(resposta['main']['temp'])
    print(resposta['main']['humidity'])
    # print(resposta['rain']['1h']) # quando nao ha chuva esse da erro
    print(resposta.get('rain', {}).get('1h',0)) # Melhor forma quando existe a possibilidade da propriedade nao existir
    print(resposta['sys']['sunrise'])
    print(resposta['sys']['sunset'])

get_temp(api,'Maputo')