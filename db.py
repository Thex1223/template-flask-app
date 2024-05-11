from main import *
import mysql.connector



class DB:
    def __init__(self, host, user, password, database):
        self.__host__ = host
        self.__user__ = user
        self.__password__ = password
        self.__database__ = database
        self.connection = None

    def connect(self):

        try:
            # Acessa o banco de dados
            self.connection = mysql.connector.connect(
                host=self.__host__,            
                user=self.__user__,
                password=self.__password__,
                database=self.__database__
            )
            self.cursor = self.connection.cursor()
            print("[LOG DB]: Sucesso à conectar ao banco de dados!")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("[LOG DB]: Acesso negado. Verifique o nome de usuário e a senha.")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("[LOG DB]: Banco de dados não existe.")

            else:
                print("[LOG DB]: Não foi possivél conectar ao banco de dados!")
                print(f"[LOG DB]: Erro => {err}")
                return False
