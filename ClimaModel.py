from pydantic import BaseModel
from typing import List
from datetime import datetime

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

