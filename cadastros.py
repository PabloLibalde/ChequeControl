from conectionbd import DataBase 

# Class inicial do cheque e suas propriedades
class Pessoas:
    def __init__(self,cpf,nome,apelido,endereco,bairro,id = 'null'):
        self.id = id
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

class Cadastrar:
    
    def pessoa(pessoa):
        
        db = DataBase
        db.connect

        resp = db.register_pessoa(pessoa)
        if resp == "OK":
            print("Pessoa Inserida no db com Sucesso")
        else:
            print(resp)

class Deletar:
    
    def pessoa(pessoa):
        
        db = DataBase
        db.connect
        
        lista = ()
        select = (db.select_all_pessoas(pessoa))
        
        for pes in select:
            if pessoa in pes:
                x = Pessoas(pes)
                print(x.id)
        
        

        resp = db.deletar_pessoa(pessoa)
        if resp == "OK":
            print("Pessoa deletada no db com Sucesso")
        else:
            print(resp)

class Teste:
    def __init__(self,cpf,nome,id = 'null'):
        self.cpf = cpf
        self.nome = nome
        self.id = id
    
