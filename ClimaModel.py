from pydantic import BaseModel
from typing import List
from datetime import datetime

from ClimaService import getDadosClima, calculateSunDuration, geraRecomendacao


class Recomendacao(BaseModel):
    id:int
    id_previsao:int
    recomendacao:str



class Previsao(BaseModel):
    id:int
    localizacao:str
    temperatura:float
    humidade:float
    precipitacao:float
    luz_solar:int
    recomendacao:List[Recomendacao] = []
    data_registo:datetime


    @staticmethod
    def saveModelPrevisao(cidade:str):
        dadosCLimaticos = getDadosClima(cidade)

        if not dadosCLimaticos:
            print('Erro ao carregar dados do clima!')
            return

        temperatura = dadosCLimaticos['main']['temp'] - 273
        humidade = dadosCLimaticos['main']['humidity']
        precipitacao = dadosCLimaticos.get('rain', {}).get('1h', 0) * 100
        luz_solar = calculateSunDuration(cidade)

        lista_rec_str = geraRecomendacao(temperatura, humidade, precipitacao, cidade)
        lista_rec = [Recomendacao(id=0, id_previsao=0, recomendacao=rec) for rec in lista_rec_str]

        previsao = Previsao(
            id=0,
            localizacao=cidade,
            temperatura=temperatura,
            humidade=humidade,
            precipitacao=precipitacao,
            luz_solar=luz_solar,
            recomendacao=lista_rec,
            data_registo=datetime.now()
        )
        return previsao



