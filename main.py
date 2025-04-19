
from fastapi import FastAPI
from typing import List

from ClimaDao import ClimaDao
from ClimaModel import Previsao

app = FastAPI()

@app.get("/previsoes", response_model=List[Previsao])
def listar_previsoes():
    dao = ClimaDao()
    return dao.consultaPrevisa()

@app.get("/previsoes/{local}", response_model=List[Previsao])
def getPrevisoes(local:str):
    dao = ClimaDao()
    return dao.consultaPrevisaPorRegiao(local)


@app.post("/previsao/{cidade}")
def criar_previsao(cidade:str):
    previsao = Previsao.saveModelPrevisao(cidade)
    dao = ClimaDao()
    dao.savePrevisao(previsao)
    return {"mensagem": "Previsão salva com sucesso"}