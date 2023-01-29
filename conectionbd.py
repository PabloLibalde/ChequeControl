import sqlite3

banco = 'cheques.db'


#Criando conexao


class DataBase:
    def __init__(self, name = f'{banco}'):
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            return "Erro Conexao"
        
    def create_table_pessoas(self):
        connection = sqlite3.connect(banco)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                ID INTEGER NOT NULL PRIMARY KEY,
                CPF TEXT,
                NOME TEXT,
                APELIDO TEXT,
                ENDERECO TEXT,
                BAIRRO TEXT
                )
                            """)
        
    def register_pessoa(pessoa):
        campos_pessoas = ('ID','CPF','NOME','APELIDO','ENDERECO','BAIRRO')
        valores_pessoas = ("null,?,?,?,?,?")
        connection = sqlite3.connect(banco)
        cursor = connection.cursor()
        try:
            #Inseri o registro no BD
            cursor.execute(f"""INSERT INTO pessoas {campos_pessoas}
                           VALUES({valores_pessoas})""",pessoa)
            connection.commit()
            cursor.close
            return ("OK")
        except Exception as erro:
            return  (f"----Erro: conectiondb - register_pessoa ---- {erro}")
        
    def select_all_pessoas(self):
        try:
            connection = sqlite3.connect(banco)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM pessoas ORDER BY NOME")
            sql_pessoas = cursor.fetchall()
            connection.commit()
            return sql_pessoas

        except Exception as erro:
            print(erro)
            pass
        
    def select_pessoas(condicao = "id is not null" ,retorno = "*"):
        try:
            connection = sqlite3.connect(banco)
            cursor = connection.cursor()
            cursor.execute(f"SELECT {retorno} FROM pessoas WHERE {condicao} ORDER BY NOME")
            pessoas_id = cursor.fetchall()
            connection.commit()
            return pessoas_id

        except Exception as erro:
            print(erro)
            pass

    def deletar_pessoa():
        valores_pessoas = ("?,?,?,?,?")
        connection = sqlite3.connect(banco)
        cursor = connection.cursor()
        try:
            #Inseri o registro no BD
            cursor.execute("""DELETE FROM pessoas ORDER BY NOME""")
            connection.commit()
            cursor.close
            return ("OK")
        except Exception as erro:
            return  (f"----Erro: conectiondb - register_pessoa ---- {erro}")