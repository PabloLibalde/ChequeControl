from cadastros import (Pessoas,Cadastrar,Deletar)
from conectionbd import (DataBase)

p = Pessoas('null','107.978.217.67','Pablo Libalde','Pablo','Rua Argeu Resende, 96','Centro')   

db = DataBase()
db.connect()
db.create_table_pessoas()
db.close_connection()


# pessoa_input = (p.cpf,p.nome,p.apelido,p.endereco,p.bairro)
# #pessoa_input = (p.nome)


# j = (1, '107.978.217.67', 'Pablo Libalde', 'Pablo', 'Rua Argeu Resende, 96', 'Centro')


# Cadastrar.pessoa(pessoa_input)

# # print(db.select_all_pessoas())

x = db.select_all_pessoas()
for y in x:
    # print(y)
    lista =['cpf','nome','apelido','endereco','bairro','id']
    # print(lista[0])
    dic={}
    for col in y:
        print(col)
    #     p= 0
        dic[f'{lista[p]}']=col
    # print(dic)