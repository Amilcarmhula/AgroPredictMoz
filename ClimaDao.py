from ConnectionClass import ConexaoBD
from ClimaModel import Previsao, Recomendacao

class ClimaDao:

    def __init__(self):
        self.conexao = ConexaoBD().getConnection()
        self.cursor = self.conexao.cursor()

    def savePrevisao(self, p:Previsao):
        sql = """
        insert into previsao (localizacao, temperatura, humidade, precipitacao, luz_solar)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            p.localizacao,
            p.temperatura,
            p.humidade,
            p.precipitacao,
            p.luz_solar
        )
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        id_previsao = self.cursor.lastrowid

        for rec in p.recomendacao:
            self.saveRecomendacao(rec.recomendacao, id_previsao, self.cursor)

        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def saveRecomendacao(self,texto:str, id_previsao:int, cursor):
        sql = """
        insert into recomendacao (fk_id_previsao,recomendacao) 
        values (%s, %s)
        """
        valores = (id_previsao, texto)
        cursor.execute(sql, valores)


    # Metodo obsoleto
    # def consultaPrevisa(self):
    #     sql = """
    #     SELECT * FROM previsao
    #     """
    #     self.cursor.execute(sql)
    #     result = self.cursor.fetchall()
    #     # print(result)
    #     self.conexao.close()
    #     return result

    def consultaPrevisa(self) ->list[Previsao]:
        sql = """
        SELECT * FROM previsao
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        previsoes = []
        for p in result:
            previsao = Previsao(
                id=p[0],
                localizacao=p[1],
                temperatura=p[2],
                humidade=p[3],
                precipitacao=p[4],
                luz_solar=p[5],
                recomendacao=self.getRecomendacoes(p[0]),
                data_registo=p[6]
            )
            previsoes.append(previsao)

        self.conexao.close()
        return previsoes

    def getRecomendacoes(self,id_previsao:int) ->list[Recomendacao]:
        sql = "SELECT * FROM recomendacao where fk_id_previsao = %s"
        self.cursor.execute(sql, (id_previsao,))
        result = self.cursor.fetchall()
        return [Recomendacao(id=row[0],recomendacao=row[1],id_previsao=row[2]) for row in result
        ]

