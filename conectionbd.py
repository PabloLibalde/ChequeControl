import sqlite3

#Criando conexao


class DataBase:
    def __init__(self, name = 'cheques.db') -> None:
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
            CREATE TABLE IF NOT EXISTS Pessoas(
                
            PESSOA_CPF TEXT,    
            PESSOA_NOME TEXT,
            PESSOA_APELIDO TEXT,
            PESSOA_ENDERECO TEXT,
            PESSOA_BAIRRO TEXT
            
            PRIMARY_KEY(CPF)
            )
                    """)
        
    def register_pessoa(self, dadospessoas):
        pass