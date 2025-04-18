from ClimaDao import ClimaDao
from ClimaModel import Previsao, Recomendacao
from ServiceClima import getDadosClima, geraRecomendacao, calculateSunDuration
from datetime import datetime

# Teeste de insersao de previsao e recomendacoes concluida
def main():
    cidade = 'Gaza'
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
        id = 0,
        localizacao = cidade,
        temperatura = temperatura,
        humidade = humidade,
        precipitacao = precipitacao,
        luz_solar = luz_solar,
        recomendacao = lista_rec,
        data_registo = datetime.now()
    )

    dao = ClimaDao()
    dao.savePrevisao(previsao)
    print('Dados salvos com sucesso')

    dao = ClimaDao()
    prevs = dao.consultaPrevisa()
    for p in prevs:
        print(f'Para a previcaao: {p}')
        if p.recomendacao:
            for r in p.recomendacao:
                # print(f'    Temos as seguintes recomendacoes: {r}')
                print(f'    Temos as seguintes recomendacoes: {r.recomendacao}')


if __name__ == '__main__':
    main()