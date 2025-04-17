from pydantic import BaseModel
from typing import List
from datetime import datetime

class Previsao(BaseModel):
    id:int
    localizacao:str
    temperatura:float
    umidade:float
    precipitacao:float
    luz_solar:int
    recomendacoes:List[str]
    data_registo:datetime

