# AgroPredictMoz
# 🌤️ Sistema de Previsão Climática com Recomendação Agrícola

Este projeto é uma API desenvolvida com **FastAPI**, que consome dados da API **OpenWeatherMap** para gerar previsões climáticas e recomendações agrícolas com base nas condições meteorológicas de uma determinada cidade.

## 🚀 Funcionalidades

- Consulta da previsão climática para uma cidade.
- Geração automática de recomendações agrícolas com base na previsão.
- Armazenamento dos dados em banco de dados MySQL.
- Consulta das previsões registradas via API REST.

## 🧱 Estrutura do Projeto


## 🛠️ Tecnologias Utilizadas

- **FastAPI** – Framework para criação da API REST.
- **Pydantic** – Validação de dados.
- **MySQL** – Armazenamento dos dados.
- **Python dotenv** – Gerenciamento de variáveis de ambiente.
- **Requests** – Consumo da API de clima.
- **OpenWeatherMap API** – Fonte dos dados climáticos.

## ⚙️ Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Amilcarmhula/AgroPredictMoz.git
   cd AgroPredictMoz
## Crie o arquivo .env
```
DB_NAME=nome_do_banco
DB_PWD=sua_senha
API_KEY=sua_api_key_openweathermap
```
## Crie o banco de dados e tabelas no MySQL:

```
CREATE DATABASE nome_do_banco;

USE nome_do_banco;

CREATE TABLE previsao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  localizacao VARCHAR(100),
  temperatura FLOAT,
  humidade FLOAT,
  precipitacao FLOAT,
  luz_solar INT,
  data_registo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recomendacao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fk_id_previsao INT,
  recomendacao TEXT,
  FOREIGN KEY (fk_id_previsao) REFERENCES previsao(id)
);
```
## Instale as dependências:
```pip install -r requirements.txt```

## Execute o servidor:
```uvicorn main:app --reload```

## 📬 Endpoints da API

### Método	Rota	Descrição
#### Lista todas as previsões salvas

   ```GET/previsoes```

#### Cria uma nova previsão e recomendação

   ```POST/previsao/{cidade}```


## 🧠 Lógica de Recomendação
A lógica para gerar as recomendações se baseia em condições como:

      Temperatura

      Umidade

      Precipitação

      Horas de luz solar

Cada cenário climático gera recomendações específicas para práticas agrícolas.

## 📌 Observações
As unidades climáticas são convertidas de Kelvin para Celsius e milímetros por hora para porcentagem.

A API da OpenWeatherMap deve estar ativa e a API_KEY corretamente configurada no .env.

## Desenvolvido 💡 por Amilcar Mula.