from conectionbd import DataBase

# Class inicial do cheque e suas propriedades
class Pessoas:
    def __init__(self, cpf,nome,apelido,endereco,bairro):
        self.cpf = cpf
        self.nome = nome
        self.apelido = apelido
        self.endereco = endereco
        self.bairro = bairro

class Bancos:
    def __init__(self,nome):
        self.nome = nome        

class Contas:
    def __init__(self, banco,numero,agencia):
        self.banco = banco
        self.numero = numero
        self.agencia = agencia

class Cheques:
    def __init__(self, numero,banco,agencia,conta,nome):
        self.numero = numero
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.nome = nome

def cadastrar():
    db = DataBase
    db.connect
    
    dadospessoas = ('107.978.217.67','Pablo Libalde','Pablo','Rua Argeu Resende, 96','Centro')
    print(dadospessoas)
    
    resp = db.register_pessoa(dadospessoas)
    
    if resp == "OK":
        print("ok")

    
    
# pessoa = Pessoas('107.978.217.67','Pablo Libalde','Pablo','Rua Argeu Resende, 96','Centro')


db = DataBase()
db.connect()
db.create_table_pessoas()
db.close_connection()

cadastrar()

