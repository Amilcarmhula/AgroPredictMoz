from pydantic import BaseModel
import  os
from dotenv import load_dotenv
import mysql.connector


class ConexaoBD(BaseModel):
    load_dotenv()
    host: str = 'localhost'
    user: str = 'root'
    pwd: str = os.getenv('DB_PWD')
    db: str = os.getenv('DB_NAME')

    def getConnection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pwd,
            database=self.db
        )


# x = ConexaoBD()
# f = x.getConnection()
# if f.is_connected():
#     print("conextado!")
# f.close()
#
# Executando fora da classe
if __name__ == "__main__":
    conexao = ConexaoBD()

    try:
        conn = conexao.getConnection()
        if conn.is_connected():
            print("Boa Conexão!")
    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
