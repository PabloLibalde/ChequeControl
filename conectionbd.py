import sqlite3


#Criando conexao


class DataBase:
    def __init__(self, name = 'cheques.db'):
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
        
    def create_table_pessoas(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                CPF INTEGER,    
                NOME TEXT,
                APELIDO TEXT,
                ENDERECO TEXT,
                BAIRRO TEXT
                )
                            """)
        self.connection.commit
        
    def register_pessoa(self, dadospessoas):
        print(dadospessoas)
        campos_pessoas = ('CPF','NOME','APELIDO','ENDERECO','BAIRRO')
        valores_pessoas = ("?,?,?,?,?")
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""INSERT INTO pessoas {campos_pessoas}
                           VALUES({valores_pessoas})""",dadospessoas)
            self.connection.commit()
            return ("OK")
            
        except:
            return ("Erro: conectiondb - register_pessoa ")
        
    def select_all_pessoas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Pessoas ORDER BY NOME")
            pessoas = cursor.fetchall()
            return pessoas
        except:
            pass
