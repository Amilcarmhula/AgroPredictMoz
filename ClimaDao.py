from ConnectionClass import ConexaoBD
from PrevisaoModel import Previsao

class ModelDao:

    def __init__(self):
        self.conexao = ConexaoBD().getConnection()
        self.cursor = self.conexao.cursor()

    def savePrevisao(self, p:Previsao):
        sql = """
        insert into previsao (localizacao, temperatura, umidade, precipitacao, luz_solar)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            p.localizacao,
            p.temperatura,
            p.umidade,
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
