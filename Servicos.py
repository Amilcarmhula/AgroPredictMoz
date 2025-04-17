import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')



def getDadosClima(cidade:str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'
    result = requests.get(url)
    if result.status_code==200:
        return result.json()
    return None

def recomGenerator(temp: float, umidade: float, precipt: float, sun_li: int):
    recomendacoes = []

    # Condicoes para clima seco e quente com muito sol
    if temp > 32 and umidade < 40 and precipt < 10 and sun_li > 6:
        recomendacoes.append('Aumentar a frequencia de rega em curtos intervalos')
        recomendacoes.append('Usar cobertura morta para reduzir evaporacao')
        recomendacoes.append('Aplicar fertilizantes liquidos foliares no inicio da manha')

    # Condicoes para clima umido e chuvoso com baixa luminosidade
    if 20 < temp < 26 and umidade > 80 and precipt > 50 and sun_li < 3:
        recomendacoes.append('Suspender a rega ou reduzir a rega ao minimo necessario')
        recomendacoes.append('Evitar fertilizantes nitrogenados')
        recomendacoes.append('Preferir adubos ricos em potassio e calcio para fortalecer as plantas')

    # Condicoes ideais para crescimento
    if 24 < temp < 28 and 55 < umidade < 70 and 20 < precipt < 40 and 4 < sun_li < 6:
        recomendacoes.append('Manter a rega regular (1 vez ao dia ou conforme o tipo de solo)')
        recomendacoes.append('Fazer adubacao equilibrada')

    # Condicoes para clima frio e úmido com muita chuva
    if temp < 20 and umidade > 80 and precipt > 60:
        recomendacoes.append('Evitar regas excessivas')
        recomendacoes.append('Utilizar fertilizantes ricos em fósforo e potássio')
        recomendacoes.append('Monitorar o drenagem do solo para evitar alagamentos')

    # Condicoes para clima quente e seco com baixa luminosidade
    if temp > 32 and umidade < 40 and precipt < 20 and sun_li < 3:
        recomendacoes.append('Aumentar a frequência de rega, mas em menor intensidade')
        recomendacoes.append('Usar cobertura de solo para reter umidade')
        recomendacoes.append('Aplicar fertilizantes líquidos de liberação lenta')

    # Condicoes para clima muito quente e muito úmido
    if temp > 30 and umidade > 90:
        recomendacoes.append('Evitar rega por aspersão, preferir rega localizada')
        recomendacoes.append('Adicionar cobertura de solo para reduzir evaporação')
        recomendacoes.append('Aplicar fungicidas preventivos')

    # Condições de clima ameno com boa luminosidade
    if 20 <= temp <= 24 and 40 < umidade < 60 and 10 < precipt < 20 and sun_li >= 6:
        recomendacoes.append('Regar de forma equilibrada, conforme o tipo de solo')
        recomendacoes.append('Aplicar adubo balanceado')

    return recomendacoes


