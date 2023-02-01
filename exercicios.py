import sqlite3

banco = 'cheque.db'

#Criando conexao


        

connection = sqlite3.connect(banco)
cursor = connection.cursor() 
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            CPF INTEGER NOT NULL PRIMARY KEY,    
            NOME TEXT,
            APELIDO TEXT,
            ENDERECO TEXT,
            BAIRRO TEXT
            )
                        """)
    print("Ok")
except Exception as erro:
    print(erro)
# x = 
try:
    cursor.execute(f"""INSERT INTO pessoas (CPF,NOME,APELIDO,ENDERECO,BAIRRO)
                            VALUES (null,?,?,?,?)""",('a','b','c','d'))
    connection.commit()
    print('Inserido com Sucesso')
except Exception as erro:
    print(erro)

try:
    cursor.execute("""
                   SELECT * FROM pessoas """
                   )
    row = (cursor.fetchall())
    print(row)
except Exception as erro:
    print(erro)
