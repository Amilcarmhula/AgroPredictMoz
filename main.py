
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from ClimaDao import ClimaDao
from ClimaModel import Previsao

app = FastAPI()

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:5173"],  # ou use ["*"] durante o desenvolvimento
    allow_origins=["*"],  # ou use ["*"] durante o desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET de dados climaticos de uma regiao para serem mostrados para o usuario
@app.get('/clima/regiao/{local}', response_model=Previsao)
def getLastClima(local:str):
    clima = ClimaDao()
    return clima.getClima(local)

# Lista todas previsoes
@app.get("/previsao/all", response_model=List[Previsao])
def listar_previsoes():
    dao = ClimaDao()
    return dao.consultaPrevisa()

# Lista todas previsoes segundo a regiao. Ideal para historico
@app.get("/previsao/all/{local}", response_model=List[Previsao])
def getPrevisoes(local:str):
    dao = ClimaDao()
    return dao.consultaPrevisaPorRegiao(local)

# Salva previsao da regiao no banco de dados
@app.post("/add/previsao/{cidade}")
def criar_previsao(cidade:str):
    previsao = Previsao.saveModelPrevisao(cidade)
    dao = ClimaDao()
    dao.savePrevisao(previsao)
    return {"mensagem": "Previsão salva com sucesso"}