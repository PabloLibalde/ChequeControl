import sqlite3 as lite

#Criando conexao
con = lite.connect('cheques.db')
print("Conexao bem Sucedida!")
cur = con.cursor()

# Class inicial do cheque e suas propriedades
class Pessoas:
    def __init__(self, pessoa_nome,pessoa_apelido,pessoa_endereco,pessoa_bairro):
        self.pessoa_nome = pessoa_nome
        self.pessoa_apelido = pessoa_apelido
        self.pessoa_endereco = pessoa_endereco
        self.pessoa_bairro = pessoa_bairro

class Bancos:
    def __init__(self,banco_nome):
        self.banco_nome = banco_nome        

class Contas:
    def __init__(self, conta_banco,conta_numero,conta_agencia):
        self.conta_banco = conta_banco
        self.conta_numero = conta_numero
        self.conta_agencia = conta_agencia

class Cheques:
    def __init__(self, cheque_numero,cheque_banco,cheque_agencia,cheque_conta,cheque_nome):
        self.cheque_numero = cheque_numero
        self.cheque_banco = cheque_banco
        self.cheque_agencia = cheque_agencia
        self.cheque_conta = cheque_conta
        self.cheque_nome = cheque_nome

    
    def cadastrar_cheque(self,):
        query = "INSERT INTO "
